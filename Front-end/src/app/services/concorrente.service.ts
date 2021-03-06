import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { delay, tap } from 'rxjs/operators';

import { environment } from './../../environments/environment';

import { Concorrente } from './../models/concorrente';

@Injectable({
  providedIn: 'root'
})
export class ConcorrenteService {

  constructor(private http: HttpClient) { }

  listarConcorrente(){
    return this.http.get<Concorrente[]>(`${environment.api}/concorrente`).pipe(delay(1000))
  }
}
