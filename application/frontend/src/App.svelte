<script>
  import Keyboard from './lib/Keyboard.svelte'

  let message = "";

  async function getMessage() {
    try {
      const response = await fetch('http://localhost:8800/development_message');
      const data = await response.json();
      message = data.message;
    } catch (error) {
      console.error('An error occurred:', error);
      message = 'Failed to load development message.';
    }
  }

  getMessage();
</script>

<main>
  <p>{message}</p>

  <div class="card">
    <Keyboard />
  </div>

</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
</style>
