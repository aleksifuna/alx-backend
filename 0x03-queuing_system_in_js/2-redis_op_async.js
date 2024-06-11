import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
const asyncGet = promisify(client.get).bind(client);
client.on('error', (err) => console.log('Redis client not connected to the server:', err));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const value = await asyncGet(schoolName);
  if (value) {
    console.log(value);
  }
}

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}
client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
