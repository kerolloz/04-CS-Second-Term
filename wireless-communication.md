# Wireless Communication

- Which one of the following is the common standard that defines wireless LAN
  operation?

  a. IEEE 802.1  
  b. IEEE 802.1x  
  c. IEEE 802.11  
  d. IEEE 802.3

  ```
  C. The IEEE 802.11 standard focuses on wireless LAN definitions, methods, and
  operation. It is made up of many pieces, as described in Chapter 2, “RF Standards.”
  Sometimes you might see IEEE 802.11x, which refers to the many subparts of
  802.11. Be aware of the subtle difference between that and 802.1x, which defines
  port-based network access control.
  ```

- which of the following represent the frequency bands commonly used for wireless
  LANs? (Choose two.)

  a. 2.4 MHz  
  b. 2.4 GHz  
  c. 5.5 MHz  
  d. 11 GHz  
  e. 5 GHz

  ```
  B, E. Wireless LANs use the 2.4-GHz and 5-GHz bands. Be careful to notice the
  difference between megahertz (MHz) and gigahertz (GHz). Also remember that 5.5
  Mbps and 11 Mbps are some of the common data rates used in wireless LANs, but
  those are not involved when you need to identify the frequency band.
  ```

- Two transmitters are each operating with a transmit power level of 100 mW. When
  you compare the two absolute power levels, what is the difference in dB?

  a. 0 dB  
  b. 20 dB  
  c. 100 dB  
  d. You can’t compare power levels in dB.

  ```
  A. When the two power levels are the same, the result is 0 dB. As long as you remember
  the first handy Law of Zero, you will find exam questions like this easy. If not, you
  will need to remember that dB = 10log 10 (100 mW / 100 mW) = 10log 10 (1) = 0 dB.
  ```

- A transmitter is configured to use a power level of 17 mW. One day it is reconfigured
  to transmit at a new power level of 34 mW. How much has the power level increased
  in dB?

  a. 0 dB  
  b. 2 dB  
  c. 3 dB  
  d. 17 dB  
  e. None of these answers are correct; you need a calculator to figure this out.

  ```
  C. At first glance, 17 mW and 34 mW might seem like odd numbers to work with.
  Notice that if you double 17, you get 34. The second handy dB fact says that
  doubling a power level will increase the dB value by 3.
  ```

- Transmitter A has a power level of 1 mW, and transmitter B is 100 mW. Compare
  transmitter B to A using dB, and then identify the correct answer from the following
  choices.

  a. 0 dB  
  b. 1 dB  
  c. 10 dB  
  d. 20 dB  
  e. 100 dB

  ```
  D. Start with transmitter A’s level of 1 mW and try to figure out some simple opera-
  tions that can be used to get to transmitter B’s level of 100 mW. Remember the handy
  Laws of 3s and 10s, which use multiplication by 2 and 10. In this case, 1 mW × 10 =
  10 mW × 10 = 100 mW. Each multiplication by 10 adds 10 dB, so the end result is 10
  + 10 = 20 dB. Notice that transmitter B is being compared to A (the reference level),
  which is 1 mW. You could also state the end result in dB-milliwatt (dBm).
  ```

- A transmitter normally uses an absolute power level of 100 mW. Through the course
  of needed changes, its power level is reduced to 40 mW. What is the power-level
  change in dB?

  a. 2.5 dB  
  b. 4 dB  
  c. –4 dB  
  d. –40 dB  
  e. None of these answers are correct; where is that calculator?

  ```
  C. This question involves a reduction in the power level, so the dB value must be
  negative. Try to find a simple way to start with 100 and get to 40 by multiplying or
  dividing by 2 or 10. In this case, 100 / 10 = 10; 10 × 2 = 20; 20 × 2 = 40. Dividing by
  10 reduced the dB value by 10 dB; then multiplying by 2 increased the total by +3
  dB; multiplying again by 2 increased the total by +3 more dB. In other words,
  dB = –10 + 3 + 3 = –4 dB.
  ```

- Consider a scenario with a transmitter and a receiver that are separated by some
  distance. The transmitter uses an absolute power level of 20 dBm. A cable connects the
  transmitter to its antenna. The receiver also has a cable connecting it to its antenna.
  Each cable has a loss of 2 dB. The transmitting and receiving antennas each have a gain
  of 5 dBi. What is the resulting EIRP?

  a. +20 dBm  
  b. +23 dBm  
  c. +26 dBm  
  d. +34 dBm  
  e. None of these answers are correct.

  ```
  B. Remember that the EIRP involves radiated power, and that is calculated using
  only the transmitter components. The EIRP is the sum of the transmitter power
  level (+20 dBm), the cable loss (–2 dB), and the antenna gain (+5 dBi). Therefore,
  the EIRP is +23 dBm.
  ```

- A receiver picks up an RF signal from a distant transmitter. Which one of the
  following represents the best signal quality received? Example values are given in
  parentheses.

  a. Low SNR (10 dB), Low RSSI (–75)  
  b. High SNR (30 dB), Low RSSI (–75)  
  c. Low SNR (10 dB), High RSSI (–30)  
  d. High SNR (30 dB), High RSSI (–30)

  ```
  D. A high SNR is best, where the received signal strength is more elevated above the
  noise floor. A 30-dBm SNR separates the signal from the noise more than a 10-dBm
  SNR does. Likewise, a higher RSSI value means that the signal strength alone is
  higher. The RSSI scale ranges from 0 (highest) to –100 (lowest).
  ```

- The typical data rates of 1, 2, 5.5, and 11 Mbps can be supported by which one of the
  following modulation types?

  a. OFDM  
  b. FHSS  
  c. DSSS  
  d. QAM

  ```
  C. DSSS supports 1-, 2-, 5.5-, and 11-Mbps data rates through different combinations
  of coding and modulation schemes. FHSS is locked to 1 or 2 Mbps. With the
  exception of 6 and 9 Mbps, only OFDM supports the highest data rates of all the
  modulation types.
  ```

- Put the following modulation schemes in order of the number of possible changes
  that can be made to the carrier signal, from lowest to highest.

  a. 16-QAM  
  b. DQPSK  
  c. DBPSK  
  d. 64-QAM

  ```
  C, B, A, D. The correct order is C, B, A, D or DBPSK (2 possible phase changes),
  DQPSK (4 possible phase changes), 16-QAM (16 possible phase/amplitude chang-
  es), 64-QAM (64 possible phase/amplitude changes).
  ```

- 64-QAM modulation alters which two of the following aspects of an RF signal?

  a. Frequency  
  b. Amplitude  
  c. Phase  
  d. Quadrature

  ```
  B, C. Both 16-QAM and 64-QAM alter the amplitude and phase of a signal.
  ```

- OFDM offers data rates up to 54 Mbps, but DSSS supports much lower limits.
  Compared with DSSS, which one of the following does OFDM leverage to achieve
  its superior data rates?

  a. Higher-frequency band  
  b. Wider 20-MHz channel width  
  c. 48 subcarriers in a channel  
  d. Faster chipping rates  
  e. Greater number of channels in a band

  ```
  C. OFDM uses 48 subcarriers in a single 20-MHz-wide channel, allowing it to
  transmit data bits in parallel. DSSS uses a single 22-MHz channel with only one
  main carrier signal.
  ```

- Which regulatory body allocated the 2.4–2.5-GHz band for industrial, scientific, and
  medical use?

  a. IEEE  
  b. ETSI  
  c. ITU-R  
  d. FCC

  ```
  C. The ITU-R allocated the ISM bands for global use.
  ```

- The U-NII-1 band is used for which one of the following purposes?

  a. 2.4-GHz wireless LANs  
  b. 5-GHz wireless LANs  
  c. Medical applications  
  d. Point-to-point links

  ```
  B. The U-NII-1 band is the first of four 5-GHz bands set aside for wireless LAN
  use.
  ```

- In the 2.4-GHz band, the FCC limits the EIRP of a point-to-multipoint link to which
  one of the following maximum values?

  a. 100 mW  
  b. 20 dBm  
  c. 50 mW  
  d. 36 dBm

  ```
  D. The EIRP is always limited to +36 dBm in the 2.4-GHz band, except in the case
  of point-to-point links.
  ```

- Wireless LAN operation is defined in which one of the following standards?

  a. 802.1  
  b. 802.2  
  c. 802.3  
  d. 802.11  
  e. 802.15

  ```
  D. The IEEE 802.11 standard is the official specification for wireless LAN
  operation.

  ```

- Which one of the following specifies the correct list of non-overlapping channels for
  DSSS use in the 2.4-GHz band?

  a. 1, 2, 3  
  b. 1, 5, 10  
  c. 1, 6, 11  
  d. 1, 8, 13  
  e. All of channels 1–14

  ```
  C. Only channels 1, 6, and 11 are non-overlapping. The 2.4-GHz channels are
  spaced 5 MHz apart, whereas the DSSS channel width is 22 MHz.
  ```

- The U-NII-1 band begins at which one of the following channel numbers?

  a. 0  
  b. 1  
  c. 24  
  d. 36

  ```
  D. The first U-NII-1 channel is labeled channel 36.
  ```

- Which of the following standards apply to wireless LAN operation in the 5-GHz
  band? (Choose all that apply.)

  a. IEEE 802.1  
  b. IEEE 802.11g  
  c. IEEE 802.11a  
  d. IEEE 802.11n  
  e. IEEE 802.11ac  
  f. IEEE 802.11b  
  g. IEEE 802.11-2012

  ```
  C, D, E, G. IEEE 802.11a is strictly for 5 GHz, 802.11n includes both 2.4- and
  5-GHz bands, and 802.11ac is limited to 5 GHz. The IEEE 802.11-2012 standard
  has all of these amendments rolled up into one document. IEEE 802.11g and
  802.11b deal with the 2.4-GHz band.
  ```

- Which of the following wireless LAN standards use OFDM for transmissions?
  (Choose all that apply.)

  a. 802.11-1997  
  b. 802.11b  
  c. 802.11g  
  d. 802.11a

  ```
  C, D. Both 802.11g and 802.11a define OFDM use, even though the two standards
  use different bands.
  ```

- Which one of the following correctly specifies the maximum theoretical data rate of
  the 802.11b, 802.11a, and 802.11n standards, respectively?

  a. 11 Mbps, 54 Mbps, 600 Mbps  
  b. 54 Mbps, 54 Mbps, 150 Mbps  
  c. 1 Mbps, 11 Mbps, 54 Mbps  
  d. 11 Mbps, 20 Mbps, 40 Mbps

  ```
  A. The maximum theoretical data rate of
  802.11b is 11 Mbps,
  802.11a is 54 Mbps, and
  802.11n is 600 Mbps.
  ```

- A 2×3 MIMO device correctly describes which one of the following?

  a. A device with two radios and three antennas  
  b. A device with two transmitters and three receivers  
  c. A device with two bonded channels and three spatial streams  
  d. A device with two receivers and three transmitters

  ```
  B. The device has two transmitters and three receivers. The number of spatial
  streams supported would be added after the 2×3 designation.
  ```

- An 802.11n device can aggregate channels to which one of the following maximum
  widths?

  a. 5 MHz  
  b. 20 MHz  
  c. 40 MHz  
  d. 80 MHz

  ```
  C. 802.11n is limited to aggregating two 20-MHz channels for a total width of
  40 MHz.
  ```

- Which one of the following standards can make use of multiple spatial streams on a
  transmitter and a receiver? (Choose all that apply.)

  a. 802.11n  
  b. 802.11b  
  c. 802.11g  
  d. 802.11a  
  e. 802.11ac  
  f. All of these answers are correct.

  ```
  A, E. Devices using 802.11n or 802.11ac can use multiple radio chains and multiple
  spatial streams.
  ```

- Which one of the following is the highest or best modulation scheme that can be
  used with 802.11ac devices?

  a. QPSK 3/4  
  b. 256-QAM  
  c. 128-QAM  
  d. 64-QAM  
  e. 16-QAM

  ```
  B. The 802.11ac amendment supports 256-QAM in both Wave 1 and Wave 2.
  ```

- What is the maximum number of spatial streams supported by 802.11ac?

  a. 1  
  b. 2  
  c. 4  
  d. 8  
  e. 16

  ```
  D. 802.11ac supports a maximum of eight spatial streams, although only three are
  supported in Wave 1 and four in Wave 2.
  ```

- Which one of the following organizations certifies 802.11 interoperability?

  a. ITU-R  
  b. FCC  
  c. IEEE  
  d. Wi-Fi Alliance  
  e. Cisco

  ```
  D. Only the Wi-Fi Alliance tests and certifies wireless products according to indus-
  try standards.
  ```
