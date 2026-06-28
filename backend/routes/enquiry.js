const express = require('express');
const { body } = require('express-validator');
const { handleEnquiry } = require('../controllers/enquiryController');

const router = express.Router();

router.post(
  '/enquiry',
  [
    body('name').trim().notEmpty().withMessage('Name is required'),
    body('phone').trim().notEmpty().withMessage('Phone is required'),
    body('email').isEmail().withMessage('Valid email is required'),
    body('service').optional().trim(),
    body('message').optional().trim(),
  ],
  handleEnquiry
);

module.exports = router;
