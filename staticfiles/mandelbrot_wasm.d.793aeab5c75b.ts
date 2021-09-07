/* tslint:disable */
/* eslint-disable */
/**
*/
export enum Key {
  Up,
  Down,
  Left,
  Right,
}
/**
*/
export class Application {
  free(): void;
/**
* @returns {number}
*/
  height(): number;
/**
* @returns {number}
*/
  width(): number;
/**
* @returns {Application}
*/
  static new(): Application;
/**
*/
  update(): void;
/**
*/
  reset(): void;
/**
* @param {Point} point
* @param {boolean} out
*/
  zoom(point: Point, out: boolean): void;
/**
* @param {number} direction
*/
  shift(direction: number): void;
/**
* @returns {number}
*/
  image_buffer(): number;
}
/**
*/
export class ApplicationSettings {
  free(): void;
}
/**
*/
export class Point {
  free(): void;
/**
* @param {number} x
* @param {number} y
* @returns {Point}
*/
  static new(x: number, y: number): Point;
}

export type InitInput = RequestInfo | URL | Response | BufferSource | WebAssembly.Module;

export interface InitOutput {
  readonly memory: WebAssembly.Memory;
  readonly __wbg_point_free: (a: number) => void;
  readonly point_new: (a: number, b: number) => number;
  readonly __wbg_applicationsettings_free: (a: number) => void;
  readonly __wbg_application_free: (a: number) => void;
  readonly application_height: (a: number) => number;
  readonly application_width: (a: number) => number;
  readonly application_new: () => number;
  readonly application_update: (a: number) => void;
  readonly application_reset: (a: number) => void;
  readonly application_zoom: (a: number, b: number, c: number) => void;
  readonly application_shift: (a: number, b: number) => void;
  readonly application_image_buffer: (a: number) => number;
}

/**
* If `module_or_path` is {RequestInfo} or {URL}, makes a request and
* for everything else, calls `WebAssembly.instantiate` directly.
*
* @param {InitInput | Promise<InitInput>} module_or_path
*
* @returns {Promise<InitOutput>}
*/
export default function init (module_or_path?: InitInput | Promise<InitInput>): Promise<InitOutput>;
        