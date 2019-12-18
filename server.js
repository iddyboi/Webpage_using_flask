const Twilio = require("twilio");

const client = new Twilio(
  "AC45aafa0f5f48f149a4f0371fd06d048b",
  "4a595e06b7114921b3240d86796684d0"
);

client.messages
  .list()
  .then(messages => console.log(`most recent message is ${messages[0].body}`))
  .catch(err => console.error(err));
