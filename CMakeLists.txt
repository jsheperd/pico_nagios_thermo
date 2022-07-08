cmake_minimum_required(VERSION 3.16)

include(pico-sdk/pico_sdk_init.cmake)

project(pico_nagios_thermo)

pico_sdk_init()

add_executable(pico_nagios_thermo main.cpp)

add_subdirectory(pico-onewire)


# Link with the pico stdlib
target_link_libraries(pico_nagios_thermo pico_stdlib hardware_adc pico_one_wire)

# Create map/bin/hex/uf2 files
pico_add_extra_outputs(pico_nagios_thermo)

# Enable USB serial
pico_enable_stdio_usb(pico_nagios_thermo 1)
pico_enable_stdio_uart(pico_nagios_thermo 0)
