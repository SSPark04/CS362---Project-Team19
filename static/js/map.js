import { getEvents } from './api.js';

// initialize Leaflet map centered on OSU campus
const map = L.map('map').setView([44.5646, -123.2620], 15);

// load OpenStreetMap tiles
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

const markerLayer = L.layerGroup().addTo(map);

// build popup content for an event
function buildPopup(event) {
  const location = event.room
    ? `${event.building} ${event.room}`
    : event.building;
  return `
    <strong>${event.title}</strong><br>
    ${event.date} ${event.start_time}–${event.end_time}<br>
    ${location}
  `;
}

// fetch events and place a marker for each one that has valid coordinates
const defaultCenter = [44.5646, -123.2620];
const defaultZoom = 15;

function renderMarkers(events) {
    markerLayer.clearLayers();
  
    const groupedEvents = {};
    for (const event of events) {
      if (!event.latitude || !event.longitude) continue;
      const key = `${event.latitude},${event.longitude}`;
      if (!groupedEvents[key]) groupedEvents[key] = [];
      groupedEvents[key].push(event);
    }
  
    const markerCoords = [];

    for (const key in groupedEvents) {
      const evts = groupedEvents[key];
      const [lat, lng] = key.split(',').map(Number);
      markerCoords.push([lat, lng]);
  
      let popupContent = "";
      evts.forEach(e => {
        popupContent += buildPopup(e) + "<hr>";
      });
  
      L.marker([lat, lng])
        .addTo(markerLayer)
        .bindPopup(popupContent);
    }

    if (markerCoords.length > 1) {
      map.fitBounds(L.latLngBounds(markerCoords), { padding: [40, 40] });
    } else if (markerCoords.length === 1) {
      map.setView(markerCoords[0], defaultZoom);
    } else {
      map.setView(defaultCenter, defaultZoom);
    }
}

async function loadMarkers() {
  try {
    const events = await getEvents({ sort: 'date', order: 'asc' });
    renderMarkers(events);
  } catch (err) {
    console.error('Failed to load map markers:', err);
  }
}

document.addEventListener('events:filtered', (evt) => {
  renderMarkers(evt.detail || []);
});

loadMarkers();

// show user's current location on the map
if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(function (position) {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;

    var userIcon = L.divIcon({
      className: 'user-location-icon',
      html: '<div style="background:red;width:14px;height:14px;border-radius:50%;border:3px solid white;box-shadow:0 0 6px rgba(0,0,0,0.3);"></div>',
      iconSize: [20, 20],
      iconAnchor: [10, 10],
    });

    L.marker([lat, lng], { icon: userIcon })
      .addTo(map)
      .bindPopup('You are here');
  });
}