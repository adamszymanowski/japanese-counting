<script>
    import { keyPressed, handleChoiceClose } from './shared.js';
    import { get } from 'svelte/store';
    export let faceCharacter;
    let element;

    function handleChoiceOpen() {
        element.style.background = 'radial-gradient(yellow, orange)';
        keyPressed.set(faceCharacter);
        console.log('hello');
    }

</script>
  
<div class="key"
    bind:this={element}
    on:mouseout|stopPropagation={handleChoiceClose(element)}
    on:mouseenter|stopPropagation={handleChoiceClose(element)}
>
    <div class="key_face"
        on:mouseup={handleChoiceOpen}
    >{faceCharacter}</div>
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
        border-radius: 100%;
        background: radial-gradient(magenta, red);

    }
</style>