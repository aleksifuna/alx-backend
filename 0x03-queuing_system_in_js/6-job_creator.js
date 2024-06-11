import kue from 'kue';

const queue = kue.createQueue();

const jobObject = {
  phoneNumber: '0742364842',
  message: 'this is a message',
};

const job = queue.create('push_notification_code', jobObject)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
