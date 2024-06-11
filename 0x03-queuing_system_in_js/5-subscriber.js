import { createClient } from 'redis';

const client = createClient();
const subscriber = client.duplicate();

subscriber.on('error', (err) => console.log('Redis client not connected to the server:', err));

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
  subscriber.subscribe('holberton school channel', (err) => {
    if (err) {
      console.log(err);
    }
  });
  subscriber.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
      subscriber.unsubscribe(channel, (err) => {
        if (err) {
          console.log(err);
        }
        subscriber.quit();
        process.exit(0);
      });
    }
    console.log(message);
  });
});
