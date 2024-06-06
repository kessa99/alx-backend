function createPushNotificationJobs(jobs, queue) {
    if (!Array.isArray(jobs)) throw new Error('Jobs should be an array');

    jobs.forEach((jobData) => {
        const job = queue.create('push_notification_code_3', jobData).save((err) => {
            if (err) {
                console.error(`Notification job ${job.id} failed: ${err}`);
            } else {
                console.log(`Notification job created: ${job.id}`);
            }
        });
        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        });
        job.on('failed', () => {
            console.log(`Notification job ${job.id} failed`);
        });
        job.on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        })
    })
}

export default createPushNotificationJobs;