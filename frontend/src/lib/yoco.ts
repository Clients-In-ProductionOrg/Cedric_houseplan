/**
 * Yoco Payment Gateway Integration
 * Test Keys:
 * Public Key: pk_test_da8ab942DmM7Ydza2ea4
 * Secret Key: sk_test_ffce3caaGV8qEK3b095412985c13
 */

export const YOCO_PUBLIC_KEY = 'pk_test_da8ab942DmM7Ydza2ea4';

// Load Yoco script
export const loadYocoScript = (): Promise<void> => {
  return new Promise((resolve, reject) => {
    if ((window as any).Yoco) {
      resolve();
      return;
    }

    const script = document.createElement('script');
    script.src = 'https://js.yoco.com/sdk/latest/yoco.js';
    script.async = true;
    script.onload = () => resolve();
    script.onerror = () => reject(new Error('Failed to load Yoco SDK'));
    document.head.appendChild(script);
  });
};

// Initialize Yoco
export const initializeYoco = () => {
  if ((window as any).Yoco) {
    return (window as any).Yoco.config({ publicKey: YOCO_PUBLIC_KEY });
  }
  return null;
};

// Process payment with Yoco
export const processYocoPayment = async (
  amount: number,
  email: string,
  phone: string,
  name: string
): Promise<any> => {
  try {
    const yoco = (window as any).Yoco;
    if (!yoco) {
      throw new Error('Yoco SDK not loaded');
    }

    // Get the token from Yoco
    const response = await yoco.tokenize({
      publicKey: YOCO_PUBLIC_KEY,
      email,
      phone,
      name,
      amount,
    });

    return response;
  } catch (error) {
    console.error('Yoco payment error:', error);
    throw error;
  }
};

// Format amount for Yoco (Yoco expects amount in cents)
export const formatAmountForYoco = (amount: number): number => {
  return Math.round(amount * 100);
};
