<script>
    import FlickCircle from './FlickCircle.svelte';
    import Key from './Key.svelte';
    import { keyPressed } from './state.js';

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
  
<div class="keyboard">
    {#if $keyPressed === aSet.core}
        <FlickCircle inputCharacters={aSet} />
    {:else}
      <div></div>
    {/if}

    {#if $keyPressed === kaSet.core}
    <FlickCircle inputCharacters={kaSet} />
    {:else}
        <div></div>
    {/if}

    {#if $keyPressed === saSet.core}
        <FlickCircle inputCharacters={saSet} />
    {:else}
        <div></div>
    {/if}


    {#if $keyPressed === taSet.core}
        <FlickCircle inputCharacters={taSet} />
    {:else}
        <Key faceCharacter={aSet.core} />
    {/if}

    {#if $keyPressed === naSet.core}
        <FlickCircle inputCharacters={naSet} />
    {:else}
        <Key faceCharacter={kaSet.core} />
    {/if}

    {#if $keyPressed === haSet.core}
        <FlickCircle inputCharacters={haSet} />
    {:else}
        <Key faceCharacter={saSet.core} />
    {/if}


    {#if $keyPressed === maSet.core}
        <FlickCircle inputCharacters={maSet} />
    {:else}
        <Key faceCharacter={taSet.core} />
    {/if}

    {#if $keyPressed === yaSet.core}
        <FlickCircle inputCharacters={yaSet} />
    {:else}
        <Key faceCharacter={naSet.core} />
    {/if}

    {#if $keyPressed === raSet.core}
        <FlickCircle inputCharacters={raSet} />
    {:else}
        <Key faceCharacter={haSet.core} />
    {/if}
    <!--
    {#each characterSets as characters}
        <div>
            <FlickCircle inputCharacters={characters} />
        </div>
    {/each}   
{#each characterSets as characters}
    <div>
        <Key faceCharacter={characters.core} />
    </div>
{/each}
-->
</div>

<style>
    .keyboard {
        display: grid;
        grid-template-rows: 1fr 1fr 1fr 1fr 1fr;
        grid-template-columns: 1fr 1fr 1fr;
    }
</style>