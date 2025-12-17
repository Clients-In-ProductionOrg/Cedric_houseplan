/**
 * Application Configuration Constants
 */

// Backend API Base URL - REQUIRED - no fallback to localhost
const apiUrl = import.meta.env.VITE_API_URL;
if (!apiUrl) {
  throw new Error('VITE_API_URL environment variable is not set');
}
export const API_BASE_URL = apiUrl;

// API Endpoints
export const API_ENDPOINTS = {
  PLANS: `${API_BASE_URL}/api/core/plans/`,
  PLAN_DETAIL: (id: string | number) => `${API_BASE_URL}/api/core/plans/${id}/`,
  SETTINGS: `${API_BASE_URL}/api/core/settings/`,
  CONTACTS: `${API_BASE_URL}/api/core/contacts/`,
  QUOTES: `${API_BASE_URL}/api/core/quotes/`,
};

// Frontend URL
const frontendUrl = import.meta.env.VITE_FRONTEND_URL;
export const FRONTEND_URL = frontendUrl || 'https://cedric-houseplan2.vercel.app';
