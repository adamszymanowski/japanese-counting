import { writable, get } from 'svelte/store';

export const keyPressed = writable('');

export function handleChoiceClose(element) {
    if (get(keyPressed) === '') { return ;} // early return
    element.style.background = 'radial-gradient(red, yellow)';
    console.log('bye!');
    keyPressed.set('');
}
