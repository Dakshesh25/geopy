import streamlit as st
from geopy.geocoders import Nominatim
st.title("Geocoding and Reverse Geocoding App")

st.header("select mode")

geolocator = Nominatim(user_agent = "streamlit_geoapi")

mode = st.radio(
    "choose option",
    ["reverse geocoding(lat,lon --->Address)",
     "forward geocoding(Address --->Lat,lon)"]
)

if mode == "reverse geocoding(lat,lon --->Address)":
    lat = st.text_input("Enter latitude", "", key="latitude_input")
    lon = st.text_input("Enter longitude", "", key="longitude_input")
    if st.button("Get address"):
        if lat and lon:
            try:
                lat = float(lat)
                lon = float(lon)
                location = geolocator.reverse((lat,lon))

                if location:
                    st.success(f"Address\n{location.address}")
                else:
                    st.warning("no address found")
            except:
                st.error("invalid latitude or longitude")
else:
    address = st.text_input("Enter address:","")

    if st.button("Get coordinates"):
        if address:
            location = geolocator.geocode(address)
            st.write(location)
            print(dir(location))

            if location:
                st.success(f"Latitude:{location.latitude}\n,Longitude:{location.longitude}")

            else:
                st.warning("no corrdinates found for this address.")
        else:
            st.warning("Please enter an address.")
































