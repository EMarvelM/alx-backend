import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => {
  console.log('Redis client connected to the server');
  client.set('key', 'value');
});


function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

const getAsyn = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const res = await getAsyn(schoolName)
    console.log(res)
  } catch (err) {
    console.log(err)
  }
}



displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
