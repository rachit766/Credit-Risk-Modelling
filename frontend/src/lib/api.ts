import axios from 'axios';
import type { FormData, PredictionResponse } from '@/types';

const API_URL = 'https://credit-risk-modelling-n739.onrender.com';

export async function predictCreditRisk(
  data: FormData
): Promise<PredictionResponse> {
  const response = await axios.post<PredictionResponse>(
    `${API_URL}/predict`,
    data
  );

  return response.data;
}