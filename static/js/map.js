import { getEvents } from './api.js';

// initialize Leaflet map centered on OSU campus
const map = L.map('map').setView([44.5646, -123.2620], 15);

// load OpenStreetMap tiles
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

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
async function loadMarkers() {
  try {
    const events = await getEvents();

    for (const event of events) {
      // skip virtual or unset coordinates
      if (!event.latitude || !event.longitude) continue;

      L.marker([event.latitude, event.longitude])
        .addTo(map)
        .bindPopup(buildPopup(event));
    }
  } catch (err) {
    console.error('Failed to load map markers:', err);
  }
}

loadMarkers();