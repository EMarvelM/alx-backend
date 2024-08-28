import { createClient, print } from 'redis';

const client = createClient();
client.flushall()

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => {
  console.log('Redis client connected to the server');
  const objs = {
    'Portland': '50',
    'Seattle': '80',
    'New York': '20',
    'Bogota': '20',
    'Cali': '40',
    'Paris': '2',
  }
  
  let obj
  for (obj in objs) {
    client.hset('HolbertonSchools', obj, objs[obj], (err, reply) => {
        console.log('reply:', reply);
    });
  }
  
  client.hgetall('HolbertonSchools', (err, reply) => {
    console.log(reply);
  });    
});

