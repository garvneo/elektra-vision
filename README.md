# Elektra: A Vision

## Overview

Elektra is an innovative assistive technology designed to enhance the independence and daily lives of visually impaired individuals. Utilizing Python, machine learning (ML), and Raspberry Pi, Elektra provides audio object identification capabilities, empowering users with real-time information about their surroundings. [**see elektra presentation file and other docs for better understanding**]

## Features

- **Object Identification:** Elektra employs machine learning algorithms for face and vehicle detection, enabling users to recognize individuals and vehicles in their vicinity.
- **Obstacle Detection:** Utilizing ultrasonic sensors, Elektra calculates distances from obstacles or objects, providing users with vital information for navigation.
- **Home Appliance Control:** Integrated with Internet of Things (IoT) technology, Elektra can control home appliances, offering users the ability to switch lights or fans on and off with voice commands.

## Technical Details

- **Hardware:** Elektra is built on Raspberry Pi 3B+ Model, offering robust processing capabilities in a compact form factor.
- **Sensors:** Ultrasonic sensors are utilized for proximity calculation, ensuring accurate obstacle detection.
- **Algorithm:** Harr Cascade feature-based classification algorithm is employed for face and vehicle detection, delivering reliable results in real-time scenarios.

## Future Enhancements

In the future, Elektra aims to expand its functionality by integrating with mobile applications. This enhancement will enable users to scan and convert documents into speech, further enhancing accessibility and usability.

## Usage Instructions

1. **Setup:**
    - Connect Elektra to a power source and ensure all components are properly configured.
    - Launch the Elektra application on Raspberry Pi.

2. **Execution:**
    - Click on the "Run" option to initiate Elektra's functionality.

3. **Voice Commands:**
    - Elektra supports the following voice commands:
        - **Face Mode:** 
            - *Output:* Number of faces detected in front of the camera.
        - **Obstacle Mode:**
            - *Output:* Distance from the nearest obstacle.
        - **Home Appliance Control:**
            - *Output:* Confirmation of light or fan status (on/off).

## Conclusion

Elektra represents a significant advancement in assistive technology, providing visually impaired individuals with enhanced awareness of their surroundings and greater control over their environment. With its intuitive interface and innovative features, Elektra aims to improve the quality of life for its users, promoting independence and accessibility.
