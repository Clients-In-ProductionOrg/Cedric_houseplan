/**
 * Application Configuration Constants
 */

// Backend API Base URL
export const API_BASE_URL = 'http://127.0.0.1:8000';

// API Endpoints
export const API_ENDPOINTS = {
  PLANS: `${API_BASE_URL}/api/core/plans/`,
  PLAN_DETAIL: (id: string | number) => `${API_BASE_URL}/api/core/plans/${id}/`,
  SETTINGS: `${API_BASE_URL}/api/core/settings/`,
  CONTACTS: `${API_BASE_URL}/api/core/contacts/`,
  QUOTES: `${API_BASE_URL}/api/core/quotes/`,
};

// Frontend URL
export const FRONTEND_URL = 'http://localhost:8080';
