<script>
    import FlickCircle from './FlickCircle.svelte';

    export let char;
    export let selected = false;
    
    function handleClick() {
      selected = true;
    }
    
    function handleFlick() {
      selected = false;
    }
</script>
  
<button on:click={handleClick} class:selected={selected}>
    A
    <!-- 
    {#if selected}
    TODO: Render FlickCircle after clicking a key.
        <FlickCircle {char} on:flick={handleFlick} />
    {/if}
    -->
</button>
  