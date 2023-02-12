Meross Smart Bulb Add-on for Home Assistant
This is a custom component for Home Assistant that integrates with the Meross Smart Bulb.

Installation
To install this addon, follow these steps:

Copy the code from the previous example into the appropriate files on your Home Assistant system.

Create the homeassistant-meross-smart-bulb directory in the custom_components directory of your Home Assistant installation.

Save the manifest.json, requirements.txt, and meross_smart_bulb.py files into the homeassistant-meross-smart-bulb directory.

Restart Home Assistant to apply the changes.

Go to the Home Assistant UI and navigate to the "Configuration" section.

Click on "Integrations".

In the "Integrations" page, click on the "+" icon to add a new integration.

In the search bar, type "Meross Smart Bulb" and select it from the list of results.

Follow the prompts to enter your Meross credentials and configure the integration.

Finally, restart Home Assistant again to apply the changes and the Meross smart bulb should now be available in the list of entities.

Usage
Once the Meross Smart Bulb is integrated with Home Assistant, you can control it using the Home Assistant UI or by using automations.

The Meross Smart Bulb will appear as a light entity in Home Assistant, and you can use the standard light controls to turn it on/off, adjust brightness, and set color temperature.

Troubleshooting
If you run into any issues or errors while installing or using this addon, check the Home Assistant logs for more information. If you're unable to resolve the issue, feel free to create an issue on the GitHub repository or ask for help in the Home Assistant forums.
