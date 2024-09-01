# BlockShop: Blockchain-Based E-Commerce Platform

## Overview

BlockShop is an innovative e-commerce platform designed to enhance online shopping by integrating blockchain technology. Our platform tackles online fraud and review tampering issues, ensuring that reviews are genuine and reliable. By leveraging smart contracts, BlockShop ensures that product reviews are tamper-proof, and users are incentivized to leave honest feedback through a rewards system. With a user-friendly interface built in React and a secure backend developed with Django REST Framework, BlockShop offers a seamless and trustworthy shopping experience.

## Features

- **Tamper-Proof Reviews**: Reviews are stored on the blockchain to prevent any modifications, ensuring authenticity and integrity.
- **One-Click Login**: Users can log in effortlessly using their MetaMask ID, streamlining the authentication process.
- **Loyalty Points**: Users earn loyalty points for writing reviews, which can be redeemed for discounts on future purchases.
- **Purchase Verification**: Reviews can only be submitted after purchasing the product, ensuring only verified feedback.
- **Dynamic Web Pages**: The front-end is designed using React for a responsive and engaging user experience.
- **Secure Payments**: Integrated various payment options to cater to diverse user preferences.

## Technology Stack

- **Blockchain**: Ethereum, Solidity (for smart contracts)
- **Frontend**: React
- **Backend**: Django REST Framework
- **Authentication**: MetaMask
- **Payment Integration**: Multiple payment gateways

## Installation

### Prerequisites

- Node.js and npm
- Python and pip
- Ethereum development environment (e.g., Truffle, Hardhat)
- MetaMask extension

### Frontend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/blockshop.git
   cd blockshop/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/blockshop.git
   cd blockshop/backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the Django server:
   ```bash
   python manage.py runserver
   ```

### Smart Contracts

1. Navigate to the smart contracts directory:
   ```bash
   cd blockshop/smart-contracts
   ```

2. Install Truffle or Hardhat:
   ```bash
   npm install -g truffle
   ```

3. Compile and deploy smart contracts:
   ```bash
   truffle compile
   truffle migrate
   ```

## Usage

1. **Register and Login**: Users can sign up or log in using MetaMask for a seamless experience.
2. **Browse Products**: Explore the product catalog and view detailed product pages.
3. **Purchase Items**: Add items to the cart and proceed to checkout using integrated payment options.
4. **Leave Reviews**: After purchasing, write a review for the product. Reviews are verified on the blockchain.
5. **Earn and Redeem Loyalty Points**: Write reviews to earn loyalty points and redeem them for discounts.

## Contributing

We welcome contributions to BlockShop! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.
