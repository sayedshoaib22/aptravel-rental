require('dotenv').config();
const express = require('express');
const cors = require('cors');
const enquiryRouter = require('./routes/enquiry');

const app = express();

// Configure CORS to allow frontend hosts
const allowedOrigins = [
  'https://aptravelrental.in',
  'https://www.aptravelrental.in',
  'http://localhost:5173',
  'http://localhost:3000'
];

app.use(cors({
  origin: allowedOrigins,
  credentials: true
}));

app.use(express.json());

// Simple request logger
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} ${req.method} ${req.url}`);
  next();
});

app.use('/api', enquiryRouter);

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ success: true, message: 'Backend is running' });
});

// Global error handler
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err && err.stack ? err.stack : err);
  res.status(500).json({ success: false, message: 'Internal server error' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app;
