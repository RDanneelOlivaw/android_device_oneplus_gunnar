#!/bin/bash
#
# SPDX-FileCopyrightText: 2016 The CyanogenMod Project
# SPDX-FileCopyrightText: 2017-2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

function blob_fixup() {
    case "${1}" in
        vendor/lib64/sensors.ssc.so)
            [ "$2" = "" ] && return 0
            sed -i "s/qti.sensor.wise_light/android.sensor.light\x00/" "${2}"
            "${SIGSCAN}" -p "EA D3 84 52 01 41 00 91 29 00 15 CB 29 41 00 D1 29 15 C9 93 4A 3F A0 72" -P "AA 00 80 52 01 41 00 91 29 00 15 CB 29 41 00 D1 29 15 C9 93 0A 00 A0 72" -f "${2}"
            ;;
        *)
            return 1
            ;;
    esac

    return 0
}

function blob_fixup_dry() {
    blob_fixup "$1" ""
}

# If we're being sourced by the common script that we called,
# stop right here. No need to go down the rabbit hole.
if [ "${BASH_SOURCE[0]}" != "${0}" ]; then
    return
fi

set -e

export DEVICE=gunnar
export DEVICE_COMMON=sm6375-common
export VENDOR=oneplus
export VENDOR_COMMON=${VENDOR}

"./../../${VENDOR_COMMON}/${DEVICE_COMMON}/extract-files.sh" "$@"
