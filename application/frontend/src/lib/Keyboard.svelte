<script>
    import FlickCircle from './FlickCircle.svelte';
    import Key from './Key.svelte';
    import { keyPressed, handleChoiceClose } from './shared.js';
    let element;

    const createInputCharacters = (characterArray) => {
        return { 
                                     up:   characterArray[2], 
            left: characterArray[1], core: characterArray[0], right: characterArray[3], 
                                     down: characterArray[4] 
        };
    }

    const aSet = createInputCharacters(["あ", "い", "う", "え", "お"]);
    const kaSet = createInputCharacters(["か", "き", "く", "け", "こ"]);
    const saSet = createInputCharacters(['さ', 'し', 'す', 'せ', 'そ']);
    const taSet = createInputCharacters(['た', 'ち', 'つ', 'て', 'と']);
    const naSet = createInputCharacters(['な', 'に', 'ぬ', 'ね', 'の']);
    const haSet = createInputCharacters(['は', 'ひ', 'ふ', 'へ', 'ほ']);
    const maSet = createInputCharacters(['ま', 'み', 'む', 'め', 'も']);
    const yaSet = createInputCharacters(['や', ' ', 'ゆ', ' ', 'よ']);
    const raSet = createInputCharacters(['ら', 'り', 'る', 'れ', 'ろ']);
    const characterSets = [aSet, kaSet, saSet, taSet, naSet, haSet, maSet, yaSet, raSet];
  </script>
  
<div class="keyboard" bind:this={element} on:mouseleave={handleChoiceClose(element)}>
    {#each characterSets as characters}
        {#if $keyPressed === characters.core}
            <FlickCircle inputCharacters={characters} />
        {:else}
            <Key faceCharacter={characters.core} />
        {/if}
    {/each}   

</div>

<style>
    .keyboard {
        display: grid;
        grid-template-rows: 1fr 1fr 1fr 1fr;
        grid-template-columns: 1fr 1fr 1fr;
    }
</style>