const API_BASE = '/api/events';

// send fetch request and return parsed JSON, throws on error
async function _request(url, options = {}) {
  const response = await fetch(url, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.error || `Request failed: ${response.status}`);
  }

  return data;
}

// fetch all events, supports filter / start / end / sort / order options
export async function getEvents(options = {}) {
  const params = new URLSearchParams();

  if (options.filter) params.set('filter', options.filter);
  if (options.start)  params.set('start',  options.start);
  if (options.end)    params.set('end',    options.end);
  if (options.sort)   params.set('sort',   options.sort);
  if (options.order)  params.set('order',  options.order);

  const query = params.toString();
  const url = query ? `${API_BASE}?${query}` : API_BASE;

  return _request(url);
}

// fetch a single event by ID
export async function getEventById(eventId) {
  return _request(`${API_BASE}/${eventId}`);
}

// create a new event
export async function createEvent(eventData) {
  return _request(API_BASE, {
    method: 'POST',
    body: JSON.stringify(eventData),
  });
}

// update an existing event by ID
export async function updateEvent(eventId, updatedFields) {
  return _request(`${API_BASE}/${eventId}`, {
    method: 'PUT',
    body: JSON.stringify(updatedFields),
  });
}

// delete an event by ID
export async function deleteEvent(eventId) {
  return _request(`${API_BASE}/${eventId}`, {
    method: 'DELETE',
  });
}

// fetch today's events sorted by start_time
export async function getTodaysEvents() {
  return getEvents({ filter: 'today', sort: 'start_time', order: 'asc' });
}

// fetch this week's events sorted by date
export async function getWeekEvents() {
  return getEvents({ filter: 'week', sort: 'date', order: 'asc' });
}

// fetch events within a custom date range
export async function getEventsByRange(startDate, endDate) {
  return getEvents({ start: startDate, end: endDate, sort: 'date', order: 'asc' });
}