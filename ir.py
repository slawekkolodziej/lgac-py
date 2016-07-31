"""
IRSend python mock
"""

def send_raw():
    """
    void  IRsend::sendRaw (const unsigned int buf[],  unsigned int len,  unsigned int hz)
    {
      // Set IR carrier frequency
      enableIROut(hz);

      for (unsigned int i = 0;  i < len;  i++) {
          if (i & 1)  space(buf[i]) ;
          else        mark (buf[i]) ;
      }

      space(0);  // Always end with the LED off
    }


    void  IRsend::space (unsigned int time)
    {
        TIMER_DISABLE_PWM; // Disable pin 3 PWM output
        if (time > 0) IRsend::custom_delay_usec(time);
    }


    void  IRsend::mark (unsigned int time)
    {
        TIMER_ENABLE_PWM; // Enable pin 3 PWM output
        if (time > 0) custom_delay_usec(time);
    }
    """
    pass


def enable_ir_out():
    """
    void  IRsend::enableIROut (int khz)
    {
      // Disable the Timer2 Interrupt (which is used for receiving IR)
      TIMER_DISABLE_INTR; //Timer2 Overflow Interrupt

      pinMode(TIMER_PWM_PIN, OUTPUT);
      digitalWrite(TIMER_PWM_PIN, LOW); // When not sending PWM, we want it low

      // COM2A = 00: disconnect OC2A
      // COM2B = 00: disconnect OC2B; to send signal set to 10: OC2B non-inverted
      // WGM2 = 101: phase-correct PWM with OCRA as top
      // CS2  = 000: no prescaling
      // The top value for the timer.  The modulation frequency will be SYSCLOCK / 2 / OCR2A.
      TIMER_CONFIG_KHZ(khz);
    }


    #define TIMER_CONFIG_KHZ(val) ({ \
        const uint8_t pwmval = SYSCLOCK / 2000 / (val); \
        TCCR2A               = _BV(WGM20); \
        TCCR2B               = _BV(WGM22) | _BV(CS20); \
        OCR2A                = pwmval; \
        OCR2B                = pwmval / 3; \
    })
    """
    pass
