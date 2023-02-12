# Meross Smart Bulb Add-on for Home Assistant

This is a custom component for [Home Assistant](https://www.home-assistant.io/) that integrates with the [Meross Smart Bulb](https://meross.com/products/smart-bulb/).

## Installation

To install this addon, follow these steps:

1. Copy the code from the previous example into the appropriate files on your Home Assistant system.

2. Create the `homeassistant-meross-smart-bulb` directory in the `custom_components` directory of your Home Assistant installation.

3. Save the `manifest.json`, `requirements.txt`, and `meross_smart_bulb.py` files into the `homeassistant-meross-smart-bulb` directory.

4. Restart Home Assistant to apply the changes.

5. Go to the Home Assistant UI and navigate to the "Configuration" section.

6. Click on "Integrations".

7. In the "Integrations" page, click on the "+" icon to add a new integration.

8. In the search bar, type "Meross Smart Bulb" and select it from the list of results.

9. Follow the prompts to enter your Meross credentials and configure the integration.

10. Finally, restart Home Assistant again to apply the changes and the Meross smart bulb should now be available in the list of entities.

## Usage

Once the Meross Smart Bulb is integrated with Home Assistant, you can control it using the Home Assistant UI or by using automations.

The Meross Smart Bulb will appear as a light entity in Home Assistant, and you can use the standard light controls to turn it on/off, adjust brightness, and set color temperature.

## Troubleshooting

If you run into any issues or errors while installing or using this addon, check the [Home Assistant logs](https://www.home-assistant.io/docs/troubleshooting/checking-the-logs/) for more information. If you're unable to resolve the issue, feel free to [create an issue](https://github.com/openai/home-assistant-meross-smart-bulb) on the GitHub repository.
