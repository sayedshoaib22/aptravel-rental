const { validationResult } = require('express-validator');
const nodemailer = require('nodemailer');

exports.handleEnquiry = async (req, res) => {
  console.log('Received enquiry:', req.body);
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    console.log('Validation errors:', errors.array());
    return res.status(400).json({ success: false, message: 'Validation failed', errors: errors.array() });
  }

  const { name, phone, email, service, message } = req.body;
  const recipient = process.env.EMAIL_USER || 'info@apcargos.in';

  try {
    const transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST || 'smtp.hostinger.com',
      port: Number(process.env.SMTP_PORT) || 465,
      secure: String(process.env.SMTP_SECURE).toLowerCase() === 'true',
      auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS,
      },
    });

    // Verify transporter config (useful for debugging)
    try {
      await transporter.verify();
      console.log('SMTP verified');
    } catch (vErr) {
      console.error('SMTP verify failed:', vErr && vErr.stack ? vErr.stack : vErr);
      // continue — sendMail will surface errors too
    }

    const mailOptions = {
      from: `${name} <${email}>`,
      to: recipient,
      subject: 'New Website Enquiry',
      text:
        `Name: ${name}\nPhone: ${phone}\nEmail: ${email}\nService: ${service || ''}\nMessage:\n${message || ''}`,
    };

    const info = await transporter.sendMail(mailOptions);
    console.log('Email sent:', info && info.messageId ? info.messageId : info);
    return res.json({ success: true, message: 'Enquiry sent successfully' });
  } catch (err) {
    console.error('Failed to send enquiry:', err && err.stack ? err.stack : err);
    // expose server error details in logs but not to client
    return res.status(500).json({ success: false, message: 'Failed to send enquiry', error: String(err) });
  }
};
