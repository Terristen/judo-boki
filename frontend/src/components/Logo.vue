<template>
    <div id="app">
        <!-- Your existing content here -->

        <!-- Floating logo in the top-right corner -->
        <img src="/assets/images/logo.webp" alt="Logo" class="floating-logo" />
    </div>
</template>

<script>
    export default {
    // Your component logic here
    };
</script>

<style>
    /* Add your existing styles here */

    /* Floating logo styling */
    .floating-logo {
    position: fixed;
    top: 10px;
    right: 10px;
    width: 100px;
    height: auto;
    z-index: 1000;
    }
</style>
