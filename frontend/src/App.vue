<template>
  <div id="app" class="app-container">
    <header class="app-header">
      <h1 class="app-title">Huntsville Judo Session Check-In</h1>
    </header>
    <main class="app-main">
      <img src="/kodokan.png" alt="Logo" class="floating-logo" />
      <Kiosk />
    </main>
  </div>
</template>

<script>
import Kiosk from './components/Kiosk.vue';

export default {
  name: 'App',
  components: {
    Kiosk,
  },
};
</script>

<style>
/* CSS Variables */
:root {
  --theme-main: #ede4ce; /* Color used for component backgrounds and content-areas */
  --theme-standout: #a59b84; /* Color used for standout elements like name buttons */
  --theme-active: #8bbccc; /* Color used for active states */
  --theme-alert: #f4d82d; /* Color used for alerts and warnings */
  --theme-alert-border: #333333; /* Color used for alerts and warnings */
  --theme-text: #44362b; /* Color used for text */
  --theme-bg1: #ede4ce; /* Color used for the main background */
  --theme-bg2: #44362b; /* Color used for secondary backgrounds */
  --theme-bg3: #0e1015; /* Color used for tertiary backgrounds */
  --theme-border: #333333; /* Color used for borders */
  --theme-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Shadow used for cards and other elements */
  --theme-confirmed: #7ca77d; /* New color for confirmed members */
  --theme-confirmed-border: #333333; /* New color for confirmed members */
  --theme-scrollbar: rgba(151, 141, 114, 0.5); /* Color used for scrollbars */
}


/* Base Styles */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: var(--theme-bg3);
  color: var(--theme-text);
}

/* App Container */
.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh; /* Full height of the viewport */
  width: 90vw; /* Ensure it takes full width of the viewport */
  color: var(--theme-text);
}

/* Header */
.app-header {
  background-color: var(--theme-bg2);
  padding: 20px;
  text-align: center;
  box-shadow: var(--theme-shadow);
  flex-shrink: 1;
}

.app-title {
  margin: 0;
  font-size: 2rem;
  color: var(--theme-main);
}

/* Main Content */
.app-main {
  flex-grow: 1; /* Take up the remaining space */
  display: flex;
  justify-content: center;
  align-items: center;

  /* flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--theme-bg1);
  height: 100%; */
}

.floating-logo {
  position: fixed;
  top: 10px;
  right: 10px;
  width: 100px;
  height: auto;
  z-index: 1000;
}
</style>
