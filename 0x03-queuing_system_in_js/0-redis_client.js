import redis from 'redis';

const client = redis.createClient();
client.on('connect', () => {
    console.log('Redis client connected');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});