#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/adc.h"

#include "hardware/gpio.h"
#include "pico-onewire/api/one_wire.h"


// The built in LED
#define LED_PIN 25
#define TEMP_ADC 4
#define DS_PIN  16


const float conversion_factor = 3.3f / (1 << 12);

void showDS() {
    One_wire one_wire(DS_PIN);
    one_wire.init();
    rom_address_t address{};

    one_wire.single_device_read_rom(address);
    one_wire.convert_temperature(address, true, false);
    printf("%3.1f\n", one_wire.temperature(address));
}

void showInternal() {
    const float voltage = adc_read() * conversion_factor;
    const float temperature = 27 - (voltage - 0.706) / 0.001721;
    printf("%3.1f\n", temperature);
}

void showMenu() {
    printf("'i': show internal temperature sensor\n");
    printf("'d': show dallas temperature sensor\n");
}
/*
    A simple application to blink the LED light, and print out the temperature.
*/
int main() {
    stdio_init_all();

    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    adc_init();
    adc_gpio_init(26);
    adc_set_temp_sensor_enabled(true);

    adc_select_input(TEMP_ADC);

    char c;

    while (true) {
        c = 'x';
        c = getchar_timeout_us(1);   
        switch(c) {
            case PICO_ERROR_TIMEOUT:
                break;
            case 'i':
                showInternal();
                break;
            case 'd':
                showDS();
                break;
            case '?':
                showMenu();
                break;
        }
        // gpio_put(LED_PIN, true);
        // sleep_ms(200);
        // gpio_put(LED_PIN, false);
        // sleep_ms(200);
    }
}

