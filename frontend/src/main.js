import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

// Import the Font Awesome core
import { library } from '@fortawesome/fontawesome-svg-core';

// Import specific icons
import { faArrowUp, faArrowDown } from '@fortawesome/free-solid-svg-icons';

// Import the Font Awesome Vue component
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';


// Add icons to the library
library.add(faArrowUp, faArrowDown);

createApp(App)
    .component('font-awesome-icon', FontAwesomeIcon)
    .mount('#app')
