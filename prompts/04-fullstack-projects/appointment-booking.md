---
title: "Build a Medical Appointment Booking System"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [appointments, healthcare, fullstack, calendar]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build a medical appointment booking system.

Stack: Next.js + PostgreSQL + Twilio (SMS) + Stripe

Roles: Admin, Doctor, Patient

Features:
1. Doctors: set weekly availability, blocked dates, appointment types
2. Patients: find doctor, view calendar, book appointment
3. Appointment types: consultation (30min), follow-up (15min), procedure (60min)
4. Confirmation: email + SMS to patient and doctor
5. Reminders: 24h and 2h before (SMS + email)
6. Telemedicine: virtual appointments with video link
7. Medical records: doctor adds notes after appointment (patient can view)
8. Insurance: collect insurance info at booking
9. Cancellation: with configurable advance notice requirement
10. Waitlist: patient joins if slot becomes available
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
