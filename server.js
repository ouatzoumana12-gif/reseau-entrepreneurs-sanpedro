const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json()); // Pour parser le JSON

// Route test pour vérifier le fonctionnement du serveur
app.get('/', (req, res) => {
  res.send('Bienvenue sur l\'API du Réseau des Entrepreneurs de San Pedro 👍');
});

// Lancement du serveur
app.listen(PORT, () => {
  console.log(`Serveur lancé sur le port ${PORT}`);
});
