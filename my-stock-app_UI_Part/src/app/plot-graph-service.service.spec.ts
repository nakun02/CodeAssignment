import { TestBed } from '@angular/core/testing';

import { PlotGraphServiceService } from './plot-graph-service.service';

describe('PlotGraphServiceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: PlotGraphServiceService = TestBed.get(PlotGraphServiceService);
    expect(service).toBeTruthy();
  });
});
