import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
    try {
        const getAsync = promisify(client.get).bind(client);
        const reply = await getAsync(schoolName);
        console.log(reply);
    } catch (error) {
        console.log(`Error getting value for ${schoolName} ${error}`);
    }
};

const displaySchoolValueAndSetNew = async (schoolName) => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
};
displaySchoolValueAndSetNew();

export { client, displaySchoolValue, setNewSchool};