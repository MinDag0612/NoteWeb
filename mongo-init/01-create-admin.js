const database = db.getSiblingDB("WebNote");

database.User.updateOne(
  { email: "admin@gmail.com" },
  {
    $setOnInsert: {
      full_name: "Admin",
      email: "admin@gmail.com",
      password: "$2b$12$tn1ugujzxj4hnVURhc.TSecPXosBaVrdOvLWBDIBtLCmAJflOfdQO",
      provider: "local",
      provider_id: null,
    },
  },
  { upsert: true },
);
