import { getEvents, getTodaysEvents, getWeekEvents, getEventsByRange } from './api.js';

// format date string to "Feb 2" style
function formatDateLabel(dateStr) {
  const [year, month, day] = dateStr.split('-').map(Number);
  const date = new Date(year, month - 1, day);
  return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
}

// render event list into #eventList
function renderEventList(events) {
  const list = document.getElementById('eventList');
  list.innerHTML = '';

  if (events.length === 0) {
    list.innerHTML = '<li class="muted">No events found.</li>';
    return;
  }

  for (const event of events) {
    const li = document.createElement('li');
    const location = event.room
      ? `${event.building} ${event.room}`
      : event.building;

    li.innerHTML = `
      <strong>${formatDateLabel(event.date)}</strong>
      — ${event.title}
      <span class="muted">(${location})</span>
    `;
    list.appendChild(li);
  }
}

function notifyFilteredEvents(events) {
  document.dispatchEvent(new CustomEvent('events:filtered', {
    detail: events,
  }));
}

// render current month calendar grid, marks days with events with a red dot
function renderCalendar(events) {
  const tbody = document.getElementById('calendarBody');
  tbody.innerHTML = '';

  const eventDates = new Set(events.map((e) => e.date));

  const now = new Date();
  const year = now.getFullYear();
  const month = now.getMonth();

  const firstDay = new Date(year, month, 1).getDay();
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  const daysInPrevMonth = new Date(year, month, 0).getDate();
  const today = now.getDate();

  let day = 1;
  let nextMonthDay = 1;
  let started = false;

  for (let row = 0; row < 6; row++) {
    if (day > daysInMonth) break;

    const tr = document.createElement('tr');

    for (let col = 0; col < 7; col++) {
      const td = document.createElement('td');

      if (!started && col < firstDay) {
        // trailing days from previous month
        td.textContent = daysInPrevMonth - (firstDay - col - 1);
        td.classList.add('mutedCell');
      } else if (day > daysInMonth) {
        // leading days from next month
        td.textContent = nextMonthDay++;
        td.classList.add('mutedCell');
      } else {
        started = true;
        td.textContent = day;

        if (day === today) td.classList.add('today');

        // add dot if an event exists on this day
        const dateKey = `${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
        if (eventDates.has(dateKey)) {
          const dot = document.createElement('div');
          dot.className = 'dot';
          dot.title = 'Event on this day';
          td.appendChild(dot);
        }

        day++;
      }

      tr.appendChild(td);
    }

    tbody.appendChild(tr);
  }
}

// re-fetch and re-render on filter button click
function initFilterBar() {
  const buttons = document.querySelectorAll('.filter-btn');
  const errorEl = document.getElementById('rangeError');

  buttons.forEach((btn) => {
    btn.addEventListener('click', async () => {
      errorEl.textContent = '';
      buttons.forEach((b) => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.dataset.filter;
      let events = [];

      try {
        if (filter === 'today') {
          events = await getTodaysEvents();
        } else if (filter === 'week') {
          events = await getWeekEvents();
        } else {
          events = await getEvents({ sort: 'date', order: 'asc' });
        }
      } catch (err) {
        console.error('Failed to fetch events:', err);
        document.getElementById('eventList').innerHTML =
          `<li class="muted">Error loading events: ${err.message}</li>`;
        return;
      }

      renderEventList(events);
      renderCalendar(events);
      notifyFilteredEvents(events);
    });
  });
}

function initRangeFilter() {
  const applyBtn = document.getElementById('applyRangeBtn');
  const startInput = document.getElementById('rangeStart');
  const endInput = document.getElementById('rangeEnd');
  const buttons = document.querySelectorAll('.filter-btn');
  const errorEl = document.getElementById('rangeError');

  applyBtn.addEventListener('click', async () => {
    const start = startInput.value;
    const end = endInput.value;

    errorEl.textContent = '';

    if (!start || !end) {
      errorEl.textContent = 'Please select both start and end dates.';
      return;
    }

    if (start > end) {
      errorEl.textContent = 'Invalid range: end date must be on or after start date.';
      return;
    }

    buttons.forEach((b) => b.classList.remove('active'));

    try {
      const events = await getEventsByRange(start, end);
      renderEventList(events);
      renderCalendar(events);
      notifyFilteredEvents(events);
    } catch (err) {
      console.error('Failed to fetch range events:', err);
      errorEl.textContent = `Error loading range events: ${err.message}`;
    }
  });
}

// load all events and initialize the page on load
async function init() {
  try {
    const events = await getEvents({ sort: 'date', order: 'asc' });
    renderCalendar(events);
    renderEventList(events);
    notifyFilteredEvents(events);
  } catch (err) {
    console.error('Failed to load events on init:', err);
    document.getElementById('eventList').innerHTML =
      `<li class="muted">Error loading events: ${err.message}</li>`;
  }

  initFilterBar();
  initRangeFilter();
}

init();