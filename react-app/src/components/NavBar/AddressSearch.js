import React, { useState, useEffect } from "react";
import PlacesAutocomplete from "react-places-autocomplete";
import "./AddressSearch.css";
import PlacesComponent, {
  geocodeByAddress,
  getLatLng,
} from "react-places-autocomplete";

const AddressSearch = () => {
  const [address, setAddress] = useState("");
  //   const [coordinates, setCoordinates] = useState({ lat: null, lng: null });

  const [showAddress, setShowAddress] = useState(false);

  const closeAddress = () => {
    setShowAddress(false);
  };

  const openAddress = () => {
    if (showAddress) {
      setShowAddress(false);
    } else {
      setShowAddress(true);
    }
  };

  useEffect(() => {
    if (!showAddress) return;

    document.addEventListener("mouseEnter", closeAddress);

    return () => document.removeEventListener("mouseEnter", closeAddress);
  }, [showAddress]);

  const handleSelect = async (value) => {
    const results = await geocodeByAddress(value);
    // const latlng = await getLatLng(results[0]);
    setAddress(value);
    // setCoordinates(latlng);
  };

  return (
    <div className="address-search-container">
      <div className="address-serach-initial" onClick={openAddress}>
        1221 S Congress Ave
      </div>
      {showAddress && (
        <PlacesAutocomplete
          value={address}
          onChange={setAddress}
          onSelect={handleSelect}
          className="address-search-box"
        >
          {({
            getInputProps,
            suggestions,
            getSuggestionItemProps,
            loading,
          }) => (
            <div>
              <div className="address-search-box">
                <div className="address-search-here-text">
                  Search for a new address
                </div>
                <div className="address-search-input-container">
                  <input
                    className="address-search-input"
                    {...getInputProps({ placeholder: " Address" })}
                  />
                </div>
                <div>
                  {loading ? <div>...loading</div> : null}
                  {suggestions.map((suggestion) => {
                    const style = {
                      backgroundColor: suggestion.active
                        ? "#D3D3D3"
                        : "#ffffff",
                      padding: "100px",
                    };
                    return (
                      <div {...getSuggestionItemProps(suggestion, { style })}>
                        {suggestion.description}
                      </div>
                    );
                  })}
                </div>
              </div>
            </div>
          )}
        </PlacesAutocomplete>
      )}
    </div>
  );
};

export default AddressSearch;
