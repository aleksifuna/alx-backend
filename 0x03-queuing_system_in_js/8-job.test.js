/* eslint-env mocha */
import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  const queue = kue.createQueue();
  before(() => {
    queue.testMode.enter();
  });
  afterEach(() => {
    queue.testMode.clear();
  });
  after(() => {
    queue.testMode.exit();
  });
  it('display a error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('Alex', queue)).to.throw('Jobs is not an array');
  });
  it('create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153118782',
        message: 'This is the code 4321 to verify your account',
      },
      {
        phoneNumber: '4153718781',
        message: 'This is the code 4562 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
