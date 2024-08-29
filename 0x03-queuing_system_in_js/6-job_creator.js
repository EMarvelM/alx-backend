import kue from 'kue'

const jobObj = {
  'phoneNumber': '08083340791',
  'message': 'string',
}

const queue = kue.createQueue()
const job = queue.create('push_notification_code', jobObj).save((err) => {
  if (err) {
    console.log('Error creating job', err);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
