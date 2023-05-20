<script>
    import { keyPressed } from './state.js';
    export let faceCharacter;
    let element;

    function handleMouseUp() {
        element.style.background = 'radial-gradient(yellow, orange)';
        keyPressed.set(faceCharacter);
    }
    function handleMouseDown() {
        element.style.background = 'radial-gradient(red, yellow)';
        keyPressed.set('');
    }
</script>
  
<div class="key" 
    bind:this={element}
    on:mouseup={handleMouseUp}
    on:mousedown={handleMouseDown}
    on:mouseleave={handleMouseDown}
>
    <div class="key_face">{faceCharacter}</div>
</div>
  
<style>
    .key {
        width: var(--key-size);
        height: var(--key-size);
        display: flex;
        justify-content: center;
        align-items: center;
        background: radial-gradient(red, yellow);
        transition: background 2s ease-in-out;
    }
    .key_face {
        font-size: var(--core-radius);
    }
</style>