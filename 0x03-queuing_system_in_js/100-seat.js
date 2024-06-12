import { createClient } from 'redis';
import express from 'express';
import kue from 'kue';
import { promisify } from 'util';

const client = createClient();

function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const getAsync = promisify(client.get).bind(client);
  const number = await getAsync('available_seats');
  return number;
}

const queue = kue.createQueue();
const app = express();
const PORT = 1245;
let reservationEnabled = true;
reserveSeat(50);
app.get('/available_seats', async (req, resp) => {
  const seats = await getCurrentAvailableSeats();
  resp.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', async (req, resp) => {
  if (!reservationEnabled) {
    resp.json({ status: 'Reservation are blocked' });
    return;
  }
  const job = queue.create('reserve_seat');
  job.save((error) => {
    if (error) {
      resp.json({ status: 'Reservation failed' });
      return;
    }
    resp.json({ status: 'Reservation in process' });
  });
  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });
  job.on('failed', (error) => {
    console.log(`Seat reservation job ${job.id} failed: ${error}`);
  });
});

app.get('/process', (req, resp) => {
  queue.process('reserve_seat', async (job, done) => {
    const seats = await getCurrentAvailableSeats();
    const newSeatsNo = seats - 1;
    if (newSeatsNo === 0) {
      reservationEnabled = false;
    }
    if (newSeatsNo < 0) {
      done(new Error('Not enough seats available'));
    } else {
      reserveSeat(newSeatsNo);
      done();
    }
  });
  resp.json({ status: 'Queue processing' });
});

app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`);
});
