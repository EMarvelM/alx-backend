import { createClient, print } from "redis";

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => {
  console.log('Redis client connected to the server');
  client.set('key', 'value');
});


function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (val, rep) => console.log(rep));
}



displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
