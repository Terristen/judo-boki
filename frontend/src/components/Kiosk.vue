<template>
  <div id="app">
    <div class="kiosk-container">
      <div class="name-list-container">
        <!-- Your existing name list code -->
        <div class="name-list">
          <div 
            v-for="(student, index) in students" 
            :key="student._key" 
            :class="['name-item', { 'selected': selectedStudent && selectedStudent._key === student._key, 'confirmed': isConfirmed(student._key) }]" 
            @click="selectStudent(student)"
          >
            {{ student.first_name }} {{ student.last_name }}
          </div>
        </div>
      </div>
      <div class="detail-panel">
        <!-- Conditional rendering: show instructions or confirmation panel -->
        <div v-if="isInstructionsVisible" style="height: 100%;">
          <div v-html="instructionsHtml" class="instructionContainer"></div>
        </div>
        <div v-else>
          <h2 v-if="selectedStudent">{{ selectedStudent.first_name }} {{ selectedStudent.last_name }}</h2>
          <p v-if="selectedStudent">
            <!-- Render additional details -->
            Birthdate: {{ selectedStudent.birthdate }}<br>
            <!-- Gender: {{ selectedStudent.is_female ? 'Female' : 'Male' }}<br>
            Status: {{ selectedStudent.active ? 'Active' : 'Inactive' }}<br> -->
            Role: {{ selectedStudent.is_sensei ? 'Sensei' : 'Student' }}
          </p>
          <button 
            v-if="selectedStudent"
            class="confirm-button" 
            @click="toggleConfirmation"
          >
            {{ isConfirmed(selectedStudent._key) ? 'Cancel Confirmation' : 'Confirm' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      students: [], // Initialize an empty array for names
      selectedStudent: null,
      confirmedMembers: [],
      instructionsHtml: '', // Holds the HTML content fetched from the server
      isInstructionsVisible: true, // Determines which panel to show,
      currentSession: null
    };
  },
  mounted() {
    this.fetchStudents();
    this.fetchInstructions();
  },
  methods: {
    async fetchStudents() {
      try {
        const response = await axios.get('/api/student');
        this.students = response.data;
      } catch (error) {
        console.error('Error fetching students:', error);
      }
    },
    async fetchInstructions() {
      try {
        const response = await axios.get('/instructions.html');
        this.instructionsHtml = response.data;
      } catch (error) {
        console.error('Error fetching instructions:', error);
      }
    },
    selectStudent(student) {
      this.selectedStudent = student;
      this.isInstructionsVisible = false; // Hide instructions, show confirmation
    },
    toggleConfirmation() {
      if (this.isConfirmed(this.selectedStudent._key)) {
        this.confirmedMembers = this.confirmedMembers.filter(
          (member) => member !== this.selectedStudent._key
        );
      } else {
        this.confirmedMembers.push(this.selectedStudent._key);
      }
      this.selectedStudent = null; // Reset the confirmation panel
      this.isInstructionsVisible = true; // Show instructions again
    },
    isConfirmed(key) {
      return this.confirmedMembers.includes(key);
    }
  }
};
</script>

<style>



/* Ensure the kiosk container takes up the full height and width */
.kiosk-container {
  display: flex;
  flex-grow: 1;
  height: calc(100vh - 75.19px); /* Assuming your header is 60px tall */
  box-sizing: border-box;
  background-color: var(--theme-main);
  overflow: hidden; /* Prevent any overflow that could cause scrolling */
  width: 100%;
}

/* Make the list container scrollable and occupy the available space */
.name-list-container {
  flex-grow: 1;
  overflow-y: auto; /* Enable vertical scrolling */
  box-sizing: border-box;
  padding: 5px;
  display: flex;
  flex-direction: column;
  background-color: var(--theme-bg2);

}

/* Ensure the name list itself is scrollable within the container */
.name-list {
  flex-grow: 1; /* Make the name-list take up remaining space in the container */
  overflow-y: auto; /* Enable scrolling within this list */
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  padding-right: 10px; /* Allow space for scrollbar */
  padding-left: 5px;
  position: relative;
}

/* Custom themed scrollbar */
.name-list::-webkit-scrollbar {
  width: 12px;
}
.name-list::-webkit-scrollbar-track {
  background: var(--theme-bg2);
  border-radius: 10px;
}
.name-list::-webkit-scrollbar-thumb {
  background-color: var(--theme-border);
  border-radius: 6px;
  border: 3px solid var(--theme-bg2);
}

/* Name item styling */
.name-item {
  padding: 15px;
  margin: 10px 0;
  background-color: var(--theme-standout);
  border: 1px solid var(--theme-border);
  border-radius: 15px;
  text-align: center;
  font-size: 20px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease, border-color 0.3s ease;
}
.name-item:hover {
  background-color: var(--theme-active);
  border-color: var(--theme-active);
}
.name-item.selected {
  background-color: var(--theme-alert);
  border-color: var(--theme-alert-border);
}
/* Confirmed members have a distinct color */
.name-item.confirmed {
  background-color: var(--theme-confirmed);
  border-color: var(--theme-confirmed-border);
}

/* Style the detail panel */
.detail-panel {
  flex: 1;
  padding: 20px;
  background-color: var(--theme-bg1);
  
  box-shadow: var(--theme-shadow);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-top: 15px solid var(--theme-bg2);
  border-bottom: 15px solid var(--theme-bg2);
  border-right: 15px solid var(--theme-bg2);
  border-left: 7px solid var(--theme-bg2);
}

/* Confirm button styling */
.confirm-button {
  padding: 15px 30px;
  font-size: 20px;
  color: var(--theme-bg3);
  background-color: var(--theme-alert);
  border: 1px solid var(--theme-alert-border);
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-top: 20px;
}
.confirm-button:not(:disabled):hover {
  background-color: var(--theme-active);
}



/* Custom scrollbar for .name-list */
.name-list::-webkit-scrollbar {
  width: 20px; /* Set the width of the scrollbar */
}

.name-list::-webkit-scrollbar-track {
  background: var(--theme-scrollbar); /* Lighter shade of blue for the track */
  position: relative;
}

.name-list::-webkit-scrollbar-thumb {
  background-color:var(--theme-scrollbar); /* Lighter blue for the scrollbar thumb */
  border-radius: 10px;
  border: 4px solid transparent; /* To create some padding around the thumb */
  background-clip: padding-box;
}

/* Up Arrow */
.name-list::-webkit-scrollbar-button:vertical:start:decrement {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 512'%3E%3Cpath fill='%23978d72' d='M279 247L177 119a24 24 0 00-34 0L41 247c-9 9-4 25 11 25h192c15 0 20-16 11-25z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100%; /* Adjust size as needed */
  height: 20px; /* Set height to match the scrollbar width */
}

/* Down Arrow */
.name-list::-webkit-scrollbar-button:vertical:end:increment {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 512'%3E%3Cpath fill='%23978d72' d='M279 265L177 393a24 24 0 01-34 0L41 265c-9-9-4-25 11-25h192c15 0 20 16 11 25z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100%; /* Adjust size as needed */
  height: 20px; /* Set height to match the scrollbar width */
}


.name-list::-webkit-scrollbar-thumb:hover {
  background-color: var(--theme-scrollbar); /* Darker blue on hover */
}

.name-list::-webkit-scrollbar-corner {
  background-color: var(--theme-scrollbar); /* Match corner with the track */
}


.instructionContainer {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  width: 100%;
}

.instructionContainer h2 {
  margin-bottom: 20px;
}

/* The last p tag in instructions is pushed to the bottom */
.last-instruction {
  margin-top: auto; /* Pushes the last paragraph to the bottom */
}

</style>
