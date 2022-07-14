{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 342,
   "id": "f6dd9c2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 343,
   "id": "16f16ee1",
   "metadata": {
    "scrolled": True
   },
   "outputs": [],
   "source": [
    "datos_matrix = np.matrix('0.2 0.6 1.2 1.9 2.8 3.5 3.7 4.3 4.9 5.7 6.1 6.5; 2.36 2.55 2.89 3.34 3.98 4.87 5.65 6.83 7.92 9.44 11.04 12.89')\n",
    "datos_matrix\n",
    "\n",
    "datos = pd.DataFrame(datos_matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 344,
   "id": "b8db0982",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>X</th>\n",
       "      <th>Y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.2</td>\n",
       "      <td>2.36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.6</td>\n",
       "      <td>2.55</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.2</td>\n",
       "      <td>2.89</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.9</td>\n",
       "      <td>3.34</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2.8</td>\n",
       "      <td>3.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3.5</td>\n",
       "      <td>4.87</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>3.7</td>\n",
       "      <td>5.65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>4.3</td>\n",
       "      <td>6.83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>4.9</td>\n",
       "      <td>7.92</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>5.7</td>\n",
       "      <td>9.44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>6.1</td>\n",
       "      <td>11.04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>6.5</td>\n",
       "      <td>12.89</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      X      Y\n",
       "0   0.2   2.36\n",
       "1   0.6   2.55\n",
       "2   1.2   2.89\n",
       "3   1.9   3.34\n",
       "4   2.8   3.98\n",
       "5   3.5   4.87\n",
       "6   3.7   5.65\n",
       "7   4.3   6.83\n",
       "8   4.9   7.92\n",
       "9   5.7   9.44\n",
       "10  6.1  11.04\n",
       "11  6.5  12.89"
      ]
     },
     "execution_count": 344,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "aux = pd.DataFrame(np.asarray(datos).transpose())\n",
    "datos_dataframe = aux.rename(columns={0: \"X\", 1: \"Y\"})\n",
    "datos_dataframe"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aaaa18a7",
   "metadata": {},
   "source": [
    "# Punto a)\n",
    "\n",
    "Grafico de la nube de puntos:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 345,
   "id": "b012cef7",
   "metadata": {
    "scrolled": False
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7f8165d5f970>]"
      ]
     },
     "execution_count": 345,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(datos_dataframe['X'], datos_dataframe['Y'], 'o')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "15dce45a",
   "metadata": {},
   "source": [
    "# Punto b)\n",
    "\n",
    "Recta de minimos cuadrados:\n",
    "\n",
    "Expresion aproximante:\n",
    "$$P(x)=A_1*x+A_2$$"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b265350",
   "metadata": {},
   "source": [
    "Sistema de ecuaciones normales:\n",
    "$$A_1\\sum_{n=0}^{11}{x_i}^2+A_2\\sum_{n=0}^{11}{x_i} =\\sum_{n=0}^{11}{f({x_i}){x_i}}$$\n",
    "\n",
    "$$A_1\\sum_{n=0}^{11}{x_i}+A_2*n=\\sum_{n=0}^{11}{f({x_i})}$$\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 346,
   "id": "54f30a43",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Xi</th>\n",
       "      <th>Yi</th>\n",
       "      <th>Xi^2</th>\n",
       "      <th>Xi Yi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.2</td>\n",
       "      <td>2.36</td>\n",
       "      <td>0.04</td>\n",
       "      <td>0.472</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.6</td>\n",
       "      <td>2.55</td>\n",
       "      <td>0.36</td>\n",
       "      <td>1.530</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.2</td>\n",
       "      <td>2.89</td>\n",
       "      <td>1.44</td>\n",
       "      <td>3.468</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.9</td>\n",
       "      <td>3.34</td>\n",
       "      <td>3.61</td>\n",
       "      <td>6.346</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2.8</td>\n",
       "      <td>3.98</td>\n",
       "      <td>7.84</td>\n",
       "      <td>11.144</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3.5</td>\n",
       "      <td>4.87</td>\n",
       "      <td>12.25</td>\n",
       "      <td>17.045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>3.7</td>\n",
       "      <td>5.65</td>\n",
       "      <td>13.69</td>\n",
       "      <td>20.905</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>4.3</td>\n",
       "      <td>6.83</td>\n",
       "      <td>18.49</td>\n",
       "      <td>29.369</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>4.9</td>\n",
       "      <td>7.92</td>\n",
       "      <td>24.01</td>\n",
       "      <td>38.808</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>5.7</td>\n",
       "      <td>9.44</td>\n",
       "      <td>32.49</td>\n",
       "      <td>53.808</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>6.1</td>\n",
       "      <td>11.04</td>\n",
       "      <td>37.21</td>\n",
       "      <td>67.344</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>6.5</td>\n",
       "      <td>12.89</td>\n",
       "      <td>42.25</td>\n",
       "      <td>83.785</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Xi     Yi   Xi^2   Xi Yi\n",
       "0   0.2   2.36   0.04   0.472\n",
       "1   0.6   2.55   0.36   1.530\n",
       "2   1.2   2.89   1.44   3.468\n",
       "3   1.9   3.34   3.61   6.346\n",
       "4   2.8   3.98   7.84  11.144\n",
       "5   3.5   4.87  12.25  17.045\n",
       "6   3.7   5.65  13.69  20.905\n",
       "7   4.3   6.83  18.49  29.369\n",
       "8   4.9   7.92  24.01  38.808\n",
       "9   5.7   9.44  32.49  53.808\n",
       "10  6.1  11.04  37.21  67.344\n",
       "11  6.5  12.89  42.25  83.785"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Xi</th>\n",
       "      <th>Yi</th>\n",
       "      <th>Xi^2</th>\n",
       "      <th>Xi Yi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>41.4</td>\n",
       "      <td>73.76</td>\n",
       "      <td>193.68</td>\n",
       "      <td>334.024</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Xi     Yi    Xi^2    Xi Yi\n",
       "0  41.4  73.76  193.68  334.024"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "xi_2 = pow(datos_dataframe['X'], 2)\n",
    "xi_yi = datos_dataframe['X']*datos_dataframe['Y']\n",
    "\n",
    "tabla1 = pd.concat([datos_dataframe['X'], datos_dataframe['Y'], xi_2, xi_yi], axis=1)\n",
    "tabla1.columns = ['Xi', 'Yi', 'Xi^2', 'Xi Yi']\n",
    "\n",
    "tabla1_sums = pd.DataFrame([sum(tabla1['Xi']), sum(tabla1['Yi']), sum(tabla1['Xi^2']), sum(tabla1['Xi Yi'])]).transpose()\n",
    "tabla1_sums.columns=['Xi', 'Yi', 'Xi^2', 'Xi Yi']\n",
    "\n",
    "display(tabla1, tabla1_sums)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1f3d91d",
   "metadata": {},
   "source": [
    "Planteo de las ecuaciones normales:\n",
    "\n",
    "$$A_1*193.68+A_2*41.4=334.024$$\n",
    "$$A_1*41.4+A_2*12=73.76$$\n",
    "\n",
    "$$A_1=\\frac{334.024-A_2*41.4}{193.68}$$ \n",
    "$$A_2=\\frac{73.76-A_1*41.4}{12}$$ \n",
    "\n",
    "Formulas de Jacobi\n",
    "$$A_1^{k+1}=-A_2^k*(41.4/193.68)+(334.024/193.68)$$\n",
    "$$A_2^{k+1}=-A_1^k*(41.4/12)+(73.76/12)$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 347,
   "id": "92d9fc48",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'T de Jacobi'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.00</td>\n",
       "      <td>-0.213755</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-3.45</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      0         1\n",
       "0  0.00 -0.213755\n",
       "1 -3.45  0.000000"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'C'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.724618</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>6.146667</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          0\n",
       "0  1.724618\n",
       "1  6.146667"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'A Inicial'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   0\n",
       "0  0\n",
       "1  0"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'A a las 100 iteraciones'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.564444</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.749333</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          0\n",
       "0  1.564444\n",
       "1  0.749333"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "T_Jacobi = np.matrix([[0, -41.4/193.68],[-41.4/12, 0]])\n",
    "display(\"T de Jacobi\", pd.DataFrame(T_Jacobi))\n",
    "C_Jacobi = np.matrix([[334.024/193.68],[73.76/12]])\n",
    "display(\"C\", pd.DataFrame(C_Jacobi))\n",
    "\n",
    "A_Jacobi = np.matrix([[0],[0]])\n",
    "A_Jacobi_anterior = A_Jacobi\n",
    "display(\"A Inicial\", pd.DataFrame(A_Jacobi))\n",
    "\n",
    "for i in range(0,100):\n",
    "    A_Jacobi = T_Jacobi*A_Jacobi_anterior+C_Jacobi\n",
    "    A_Jacobi_anterior = A_Jacobi\n",
    "    \n",
    "display(\"A a las 100 iteraciones\" ,pd.DataFrame(A_Jacobi))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b332a944",
   "metadata": {},
   "source": [
    "Recta aproximante hallada:\n",
    "$$P(x)=1.564444*x+0.749333$$"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b24c15c2",
   "metadata": {},
   "source": [
    "Graficos - Recta de minimos cuadrados hallada por aproximacion + nube de puntos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 348,
   "id": "6093341a",
   "metadata": {
    "scrolled": False
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7f8165dde9e0>]"
      ]
     },
     "execution_count": 348,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x = np.linspace(0,6.5,100)\n",
    "\n",
    "y = 1.564444*x+0.749333\n",
    "\n",
    "plt.plot(x, y, '-r', label='P(x)=1.564444*x+0.749333')\n",
    "\n",
    "plt.plot(datos_dataframe['X'], datos_dataframe['Y'], 'o')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0837790f",
   "metadata": {},
   "source": [
    "# Punto c)\n",
    "\n",
    "Parabola de minimos cuadrados\n",
    "\n",
    "Expresion aproximante:\n",
    "$$P(x)=A_1*x^2+A_2x+A_3$$"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f59c0ea5",
   "metadata": {},
   "source": [
    "Sistema de ecuaciones normales:\n",
    "$$A_1\\sum_{n=0}^{11}{x_i}^4+A_2\\sum_{n=0}^{11}{x_i}^3+A_3\\sum_{n=0}^{11}{x_i}^2=\\sum_{n=0}^{11}{f({x_i}){x_i}^2}$$\n",
    "$$A_1\\sum_{n=0}^{11}{x_i}^3+A_2\\sum_{n=0}^{11}{x_i}^2+A_3\\sum_{n=0}^{11}{x_i}=\\sum_{n=0}^{11}{f({x_i}){x_i}}$$\n",
    "$$A_1\\sum_{n=0}^{11}{x_i}^2+A_2\\sum_{n=0}^{11}{x_i}+A_3*n=\\sum_{n=0}^{11}{f({x_i})}$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 349,
   "id": "cf51d562",
   "metadata": {
    "scrolled": False
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Xi</th>\n",
       "      <th>Yi</th>\n",
       "      <th>Xi^2</th>\n",
       "      <th>Xi^3</th>\n",
       "      <th>Xi^4</th>\n",
       "      <th>Xi Yi</th>\n",
       "      <th>Xi^2 Yi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.2</td>\n",
       "      <td>2.36</td>\n",
       "      <td>0.04</td>\n",
       "      <td>0.008</td>\n",
       "      <td>0.0016</td>\n",
       "      <td>0.472</td>\n",
       "      <td>0.0944</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.6</td>\n",
       "      <td>2.55</td>\n",
       "      <td>0.36</td>\n",
       "      <td>0.216</td>\n",
       "      <td>0.1296</td>\n",
       "      <td>1.530</td>\n",
       "      <td>0.9180</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.2</td>\n",
       "      <td>2.89</td>\n",
       "      <td>1.44</td>\n",
       "      <td>1.728</td>\n",
       "      <td>2.0736</td>\n",
       "      <td>3.468</td>\n",
       "      <td>4.1616</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.9</td>\n",
       "      <td>3.34</td>\n",
       "      <td>3.61</td>\n",
       "      <td>6.859</td>\n",
       "      <td>13.0321</td>\n",
       "      <td>6.346</td>\n",
       "      <td>12.0574</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2.8</td>\n",
       "      <td>3.98</td>\n",
       "      <td>7.84</td>\n",
       "      <td>21.952</td>\n",
       "      <td>61.4656</td>\n",
       "      <td>11.144</td>\n",
       "      <td>31.2032</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3.5</td>\n",
       "      <td>4.87</td>\n",
       "      <td>12.25</td>\n",
       "      <td>42.875</td>\n",
       "      <td>150.0625</td>\n",
       "      <td>17.045</td>\n",
       "      <td>59.6575</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>3.7</td>\n",
       "      <td>5.65</td>\n",
       "      <td>13.69</td>\n",
       "      <td>50.653</td>\n",
       "      <td>187.4161</td>\n",
       "      <td>20.905</td>\n",
       "      <td>77.3485</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>4.3</td>\n",
       "      <td>6.83</td>\n",
       "      <td>18.49</td>\n",
       "      <td>79.507</td>\n",
       "      <td>341.8801</td>\n",
       "      <td>29.369</td>\n",
       "      <td>126.2867</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>4.9</td>\n",
       "      <td>7.92</td>\n",
       "      <td>24.01</td>\n",
       "      <td>117.649</td>\n",
       "      <td>576.4801</td>\n",
       "      <td>38.808</td>\n",
       "      <td>190.1592</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>5.7</td>\n",
       "      <td>9.44</td>\n",
       "      <td>32.49</td>\n",
       "      <td>185.193</td>\n",
       "      <td>1055.6001</td>\n",
       "      <td>53.808</td>\n",
       "      <td>306.7056</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>6.1</td>\n",
       "      <td>11.04</td>\n",
       "      <td>37.21</td>\n",
       "      <td>226.981</td>\n",
       "      <td>1384.5841</td>\n",
       "      <td>67.344</td>\n",
       "      <td>410.7984</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>6.5</td>\n",
       "      <td>12.89</td>\n",
       "      <td>42.25</td>\n",
       "      <td>274.625</td>\n",
       "      <td>1785.0625</td>\n",
       "      <td>83.785</td>\n",
       "      <td>544.6025</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Xi     Yi   Xi^2     Xi^3       Xi^4   Xi Yi   Xi^2 Yi\n",
       "0   0.2   2.36   0.04    0.008     0.0016   0.472    0.0944\n",
       "1   0.6   2.55   0.36    0.216     0.1296   1.530    0.9180\n",
       "2   1.2   2.89   1.44    1.728     2.0736   3.468    4.1616\n",
       "3   1.9   3.34   3.61    6.859    13.0321   6.346   12.0574\n",
       "4   2.8   3.98   7.84   21.952    61.4656  11.144   31.2032\n",
       "5   3.5   4.87  12.25   42.875   150.0625  17.045   59.6575\n",
       "6   3.7   5.65  13.69   50.653   187.4161  20.905   77.3485\n",
       "7   4.3   6.83  18.49   79.507   341.8801  29.369  126.2867\n",
       "8   4.9   7.92  24.01  117.649   576.4801  38.808  190.1592\n",
       "9   5.7   9.44  32.49  185.193  1055.6001  53.808  306.7056\n",
       "10  6.1  11.04  37.21  226.981  1384.5841  67.344  410.7984\n",
       "11  6.5  12.89  42.25  274.625  1785.0625  83.785  544.6025"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Xi</th>\n",
       "      <th>Yi</th>\n",
       "      <th>Xi^2</th>\n",
       "      <th>Xi^3</th>\n",
       "      <th>Xi^4</th>\n",
       "      <th>Xi Yi</th>\n",
       "      <th>Xi^2 Yi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>41.4</td>\n",
       "      <td>73.76</td>\n",
       "      <td>193.68</td>\n",
       "      <td>1008.246</td>\n",
       "      <td>5557.788</td>\n",
       "      <td>334.024</td>\n",
       "      <td>1763.993</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Xi     Yi    Xi^2      Xi^3      Xi^4    Xi Yi   Xi^2 Yi\n",
       "0  41.4  73.76  193.68  1008.246  5557.788  334.024  1763.993"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "xi_2 = pow(datos_dataframe['X'], 2)\n",
    "xi_3 = pow(datos_dataframe['X'], 3)\n",
    "xi_4 = pow(datos_dataframe['X'], 4)\n",
    "xi_yi = datos_dataframe['X']*datos_dataframe['Y']\n",
    "xi_2_yi = xi_2*datos_dataframe['Y']\n",
    "\n",
    "tabla2 = pd.concat([datos_dataframe['X'], datos_dataframe['Y'], xi_2, xi_3, xi_4, xi_yi, xi_2_yi], axis=1)\n",
    "tabla2.columns = ['Xi', 'Yi', 'Xi^2', 'Xi^3', 'Xi^4', 'Xi Yi', 'Xi^2 Yi']\n",
    "\n",
    "tabla2_sums = pd.DataFrame([sum(tabla2['Xi']), sum(tabla2['Yi']), sum(tabla2['Xi^2']), sum(tabla2['Xi^3']), sum(tabla2['Xi^4']), sum(tabla2['Xi Yi']), sum(tabla2['Xi^2 Yi'])]).transpose()\n",
    "tabla2_sums.columns=['Xi', 'Yi', 'Xi^2', 'Xi^3', 'Xi^4', 'Xi Yi', 'Xi^2 Yi']\n",
    "\n",
    "display(tabla2, tabla2_sums)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d1861173",
   "metadata": {},
   "source": [
    "Planteo del sistema:\n",
    "\n",
    "$$A_1*5557.788+A_2*1008.246+A_3*193.68=1763.993$$\n",
    "\n",
    "$$A_1*1008.246+A_2*193.68+A_3*41.4=334.024$$\n",
    "\n",
    "$$A_1*193.68+A_2*41.4+A_3*12=73.76$$"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a79c0dab",
   "metadata": {},
   "source": [
    "Ecuaciones de Gauss-Seidel\n",
    "\n",
    "$$A_1^{K+1}=A_2^k*(-1008.246/5557.788)A_3^k*(-193.68/5557.788)+(1763.993/5557.788)$$\n",
    "\n",
    "$$A_2^{K+1}=A_1^{K+1}*(-1008.246/193.68)+A_3^k*(-41.4/193.68)+(334.024/193.68)$$\n",
    "\n",
    "$$A_3^{K+1}=A_1^{K+1}*(-193.68/12)+A_2^{K+1}*(-41.4/12)+(73.76/12)$$"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "4af0407c",
   "metadata": {},
   "source": [
    "Polinomio aproximante:\n",
    "$$P(x)=0.255529618189472*x^2-0.143398273502509x+2.51714300600557$$\n",
    "\n",
    "Graficos - Parabola de minimos cuadrados hallada por aproximacion + nube de puntos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 350,
   "id": "69f8a8ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7f81648c5810>]"
      ]
     },
     "execution_count": 350,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x = np.linspace(0,6.5,100)\n",
    "\n",
    "y = 0.255529618189472*pow(x,2)-0.143398273502509*x+2.51714300600557\n",
    "\n",
    "plt.plot(x, y, '-r', label='P(x)=0.255529618189472*x^2-0.143398273502509x+2.51714300600557')\n",
    "\n",
    "plt.plot(datos_dataframe['X'], datos_dataframe['Y'], 'o')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b87bf4f2",
   "metadata": {},
   "source": [
    "# Punto d)\n",
    "\n",
    "Modelo:\n",
    "$$y =\\frac{a}{x+b} $$"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b412aad5",
   "metadata": {},
   "source": [
    "Cambio de variables:\n",
    "$$\\frac{1}{y}=\\frac{x}{a}+\\frac{b}{a}$$\n",
    "\n",
    "$$Y=\\frac{1}{y}; A_1=\\frac{1}{a}; A_2=\\frac{b}{a}$$\n",
    "\n",
    "Ecuacion lineal propuesta\n",
    "$$Y=A_1*x+A_2$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 351,
   "id": "1cc3ddd6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>xi</th>\n",
       "      <th>Yi</th>\n",
       "      <th>xi^2</th>\n",
       "      <th>xi Yi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.2</td>\n",
       "      <td>0.423729</td>\n",
       "      <td>0.04</td>\n",
       "      <td>0.084746</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.6</td>\n",
       "      <td>0.392157</td>\n",
       "      <td>0.36</td>\n",
       "      <td>0.235294</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.2</td>\n",
       "      <td>0.346021</td>\n",
       "      <td>1.44</td>\n",
       "      <td>0.415225</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.9</td>\n",
       "      <td>0.299401</td>\n",
       "      <td>3.61</td>\n",
       "      <td>0.568862</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2.8</td>\n",
       "      <td>0.251256</td>\n",
       "      <td>7.84</td>\n",
       "      <td>0.703518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3.5</td>\n",
       "      <td>0.205339</td>\n",
       "      <td>12.25</td>\n",
       "      <td>0.718686</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>3.7</td>\n",
       "      <td>0.176991</td>\n",
       "      <td>13.69</td>\n",
       "      <td>0.654867</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>4.3</td>\n",
       "      <td>0.146413</td>\n",
       "      <td>18.49</td>\n",
       "      <td>0.629575</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>4.9</td>\n",
       "      <td>0.126263</td>\n",
       "      <td>24.01</td>\n",
       "      <td>0.618687</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>5.7</td>\n",
       "      <td>0.105932</td>\n",
       "      <td>32.49</td>\n",
       "      <td>0.603814</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>6.1</td>\n",
       "      <td>0.090580</td>\n",
       "      <td>37.21</td>\n",
       "      <td>0.552536</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>6.5</td>\n",
       "      <td>0.077580</td>\n",
       "      <td>42.25</td>\n",
       "      <td>0.504267</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     xi        Yi   xi^2     xi Yi\n",
       "0   0.2  0.423729   0.04  0.084746\n",
       "1   0.6  0.392157   0.36  0.235294\n",
       "2   1.2  0.346021   1.44  0.415225\n",
       "3   1.9  0.299401   3.61  0.568862\n",
       "4   2.8  0.251256   7.84  0.703518\n",
       "5   3.5  0.205339  12.25  0.718686\n",
       "6   3.7  0.176991  13.69  0.654867\n",
       "7   4.3  0.146413  18.49  0.629575\n",
       "8   4.9  0.126263  24.01  0.618687\n",
       "9   5.7  0.105932  32.49  0.603814\n",
       "10  6.1  0.090580  37.21  0.552536\n",
       "11  6.5  0.077580  42.25  0.504267"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>xi</th>\n",
       "      <th>Yi</th>\n",
       "      <th>xi^2</th>\n",
       "      <th>xi Yi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>41.4</td>\n",
       "      <td>2.641661</td>\n",
       "      <td>193.68</td>\n",
       "      <td>6.290077</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     xi        Yi    xi^2     xi Yi\n",
       "0  41.4  2.641661  193.68  6.290077"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "Yi = 1/datos_dataframe['Y']\n",
    "xi_2 = pow(datos_dataframe['X'], 2)\n",
    "xi_Yi = datos_dataframe['X']*Yi\n",
    "\n",
    "tabla1 = pd.concat([datos_dataframe['X'], Yi, xi_2, xi_Yi], axis=1)\n",
    "tabla1.columns = ['xi', 'Yi', 'xi^2', 'xi Yi']\n",
    "\n",
    "tabla1_sums = pd.DataFrame([sum(tabla1['xi']), sum(tabla1['Yi']), sum(tabla1['xi^2']), sum(tabla1['xi Yi'])]).transpose()\n",
    "tabla1_sums.columns=['xi', 'Yi', 'xi^2', 'xi Yi']\n",
    "\n",
    "display(tabla1, tabla1_sums)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a32d9593",
   "metadata": {},
   "source": [
    "Sistema de ecuaciones normales:\n",
    "$$A_1\\sum_{n=0}^{11}{x_i}^2+A_2\\sum_{n=0}^{11}{x_i} =\\sum_{n=0}^{11}{f({x_i}){x_i}}$$\n",
    "\n",
    "$$A_1\\sum_{n=0}^{11}{x_i}+A_2*n=\\sum_{n=0}^{11}{f({x_i})}$$"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2a9ad5d",
   "metadata": {},
   "source": [
    "Planteo de las ecuaciones normales\n",
    "\n",
    "$$A_1*193.68+A_2*41.4=6.290077$$\n",
    "$$A_1*41.4+A_2*12=2.641661$$\n",
    "\n",
    "$$A_1=\\frac{6.290077-A_2*41.4}{193.68}$$ \n",
    "$$A_2=\\frac{2.641661-A_1*41.4}{12}$$ \n",
    "\n",
    "Ecuaciones de Jacobi\n",
    "$$A_1^{k+1}=-A_2^k*(41.4/193.68)+(6.290077/193.68)$$\n",
    "$$A_2^{k+1}=-A_1^k*(41.4/12)+(2.641661/12)$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 352,
   "id": "072814d0",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'T de Jacobi'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.00</td>\n",
       "      <td>-0.213755</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-3.45</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      0         1\n",
       "0  0.00 -0.213755\n",
       "1 -3.45  0.000000"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'C'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.032477</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.220138</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          0\n",
       "0  0.032477\n",
       "1  0.220138"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'A Inicial'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   0\n",
       "0  0\n",
       "1  0"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'A a las 100 iteraciones'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-0.055529</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.411714</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          0\n",
       "0 -0.055529\n",
       "1  0.411714"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "T_Jacobi = np.matrix([[0, -(41.4/193.68)],[-(41.4/12), 0]])\n",
    "display(\"T de Jacobi\", pd.DataFrame(T_Jacobi))\n",
    "C_Jacobi = np.matrix([[(6.290077/193.68)],[(2.641661/12)]])\n",
    "display(\"C\", pd.DataFrame(C_Jacobi))\n",
    "\n",
    "A_Jacobi = np.matrix([[0],[0]])\n",
    "A_Jacobi_anterior = A_Jacobi\n",
    "display(\"A Inicial\", pd.DataFrame(A_Jacobi))\n",
    "\n",
    "for i in range(0,100):\n",
    "    A_Jacobi = T_Jacobi*A_Jacobi_anterior+C_Jacobi\n",
    "    A_Jacobi_anterior = A_Jacobi\n",
    "    \n",
    "display(\"A a las 100 iteraciones\" ,pd.DataFrame(A_Jacobi))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e65f42cc",
   "metadata": {},
   "source": [
    "Recordando:\n",
    "$$Y=\\frac{1}{y}; A_1=\\frac{1}{a}; A_2=\\frac{b}{a}$$\n",
    "\n",
    "Valores de a y b calculados\n",
    "$$-0.055529=\\frac{1}{a}$$\n",
    "\n",
    "$$0.411714=\\frac{b}{a}$$\n",
    "\n",
    "$$a=-18.008608; b=-7.414396$$"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "06a0f4f3",
   "metadata": {},
   "source": [
    "Funcion aproximante:\n",
    "$$y=\\frac{-18.008608}{x-7.414396}$$\n",
    "\n",
    "Graficos - aproximacion por modelo + nube de puntos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 353,
   "id": "7270325d",
   "metadata": {
    "scrolled": False
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7f8164773e50>]"
      ]
     },
     "execution_count": 353,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x = np.linspace(0,6.5,100)\n",
    "y = (-18.008608114678815)/(x-7.41439)\n",
    "plt.plot(x, y, '-r', label='P(x)=(-18.008608114678815/x)+2.428870')\n",
    "\n",
    "plt.plot(datos_dataframe['X'], datos_dataframe['Y'], 'o')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e461e326",
   "metadata": {},
   "source": [
    "# Punto e)\n",
    "\n",
    "Modelo:\n",
    "$$y =a*b^x $$\n",
    "\n",
    "Cambio de variables:\n",
    "$$\\ln{y}=\\ln{a}+\\ln{b}*x$$\n",
    "\n",
    "$$Y=\\ln{y}; A_1=\\ln{b}; A_2=\\ln{a}$$\n",
    "\n",
    "Ecuacion lineal propuesta\n",
    "$$Y=A_1*x+A_2$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 354,
   "id": "727da3de",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7f8164261d80>]"
      ]
     },
     "execution_count": 354,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(datos_dataframe['X'], datos_dataframe['Y'], 'o')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 355,
   "id": "1f16c3df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>xi</th>\n",
       "      <th>Yi</th>\n",
       "      <th>xi^2</th>\n",
       "      <th>xi Yi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.2</td>\n",
       "      <td>0.858662</td>\n",
       "      <td>0.04</td>\n",
       "      <td>0.171732</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.6</td>\n",
       "      <td>0.936093</td>\n",
       "      <td>0.36</td>\n",
       "      <td>0.561656</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.2</td>\n",
       "      <td>1.061257</td>\n",
       "      <td>1.44</td>\n",
       "      <td>1.273508</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.9</td>\n",
       "      <td>1.205971</td>\n",
       "      <td>3.61</td>\n",
       "      <td>2.291345</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2.8</td>\n",
       "      <td>1.381282</td>\n",
       "      <td>7.84</td>\n",
       "      <td>3.867589</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3.5</td>\n",
       "      <td>1.583094</td>\n",
       "      <td>12.25</td>\n",
       "      <td>5.540829</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>3.7</td>\n",
       "      <td>1.731656</td>\n",
       "      <td>13.69</td>\n",
       "      <td>6.407126</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>4.3</td>\n",
       "      <td>1.921325</td>\n",
       "      <td>18.49</td>\n",
       "      <td>8.261696</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>4.9</td>\n",
       "      <td>2.069391</td>\n",
       "      <td>24.01</td>\n",
       "      <td>10.140017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>5.7</td>\n",
       "      <td>2.244956</td>\n",
       "      <td>32.49</td>\n",
       "      <td>12.796249</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>6.1</td>\n",
       "      <td>2.401525</td>\n",
       "      <td>37.21</td>\n",
       "      <td>14.649303</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>6.5</td>\n",
       "      <td>2.556452</td>\n",
       "      <td>42.25</td>\n",
       "      <td>16.616937</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     xi        Yi   xi^2      xi Yi\n",
       "0   0.2  0.858662   0.04   0.171732\n",
       "1   0.6  0.936093   0.36   0.561656\n",
       "2   1.2  1.061257   1.44   1.273508\n",
       "3   1.9  1.205971   3.61   2.291345\n",
       "4   2.8  1.381282   7.84   3.867589\n",
       "5   3.5  1.583094  12.25   5.540829\n",
       "6   3.7  1.731656  13.69   6.407126\n",
       "7   4.3  1.921325  18.49   8.261696\n",
       "8   4.9  2.069391  24.01  10.140017\n",
       "9   5.7  2.244956  32.49  12.796249\n",
       "10  6.1  2.401525  37.21  14.649303\n",
       "11  6.5  2.556452  42.25  16.616937"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>xi</th>\n",
       "      <th>Yi</th>\n",
       "      <th>xi^2</th>\n",
       "      <th>xi Yi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>41.4</td>\n",
       "      <td>19.951662</td>\n",
       "      <td>193.68</td>\n",
       "      <td>82.577986</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     xi         Yi    xi^2      xi Yi\n",
       "0  41.4  19.951662  193.68  82.577986"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "Yi = np.log(datos_dataframe['Y'])\n",
    "xi_2 = pow(datos_dataframe['X'], 2)\n",
    "xi_Yi = datos_dataframe['X']*Yi\n",
    "\n",
    "tabla1 = pd.concat([datos_dataframe['X'], Yi, xi_2, xi_Yi], axis=1)\n",
    "tabla1.columns = ['xi', 'Yi', 'xi^2', 'xi Yi']\n",
    "\n",
    "tabla1_sums = pd.DataFrame([sum(tabla1['xi']), sum(tabla1['Yi']), sum(tabla1['xi^2']), sum(tabla1['xi Yi'])]).transpose()\n",
    "tabla1_sums.columns=['xi', 'Yi', 'xi^2', 'xi Yi']\n",
    "\n",
    "display(tabla1, tabla1_sums)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6724b65b",
   "metadata": {},
   "source": [
    "Sistema de ecuaciones normales:\n",
    "$$A_1\\sum_{n=0}^{11}{x_i}^2+A_2\\sum_{n=0}^{11}{x_i} =\\sum_{n=0}^{11}{f({x_i}){x_i}}$$\n",
    "\n",
    "$$A_1\\sum_{n=0}^{11}{x_i}+A_2*n=\\sum_{n=0}^{11}{f({x_i})}$$"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "979374f4",
   "metadata": {},
   "source": [
    "Planteo de ecuaciones normales\n",
    "$$A_1*193.68+A_2*41.4=82.577986$$\n",
    "$$A_1*41.4+A_2*12=19.951662$$\n",
    "\n",
    "$$A_1=\\frac{82.577986-A_2*41.4}{193.68}$$ \n",
    "$$A_2=\\frac{19.951662-A_1*41.4}{12}$$ \n",
    "\n",
    "Ecuaciones de Jacobi\n",
    "$$A_1^{k+1}=-A_2^k*(41.4/193.68)+(82.577986/193.68)$$\n",
    "$$A_2^{k+1}=-A_1^k*(41.4/12)+(19.951662/12)$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 356,
   "id": "7bf726c7",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'T de Jacobi'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.00</td>\n",
       "      <td>-0.213755</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-3.45</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      0         1\n",
       "0  0.00 -0.213755\n",
       "1 -3.45  0.000000"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'C'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.426363</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1.662638</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          0\n",
       "0  0.426363\n",
       "1  1.662638"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'A Inicial'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   0\n",
       "0  0\n",
       "1  0"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'A a las 100 iteraciones'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.270300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.730104</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          0\n",
       "0  0.270300\n",
       "1  0.730104"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "T_Jacobi = np.matrix([[0, -(41.4/193.68)],[-(41.4/12), 0]])\n",
    "display(\"T de Jacobi\", pd.DataFrame(T_Jacobi))\n",
    "C_Jacobi = np.matrix([[(82.577986/193.68)],[(19.951662/12)]])\n",
    "display(\"C\", pd.DataFrame(C_Jacobi))\n",
    "\n",
    "A_Jacobi = np.matrix([[0],[0]])\n",
    "A_Jacobi_anterior = A_Jacobi\n",
    "display(\"A Inicial\", pd.DataFrame(A_Jacobi))\n",
    "\n",
    "for i in range(0,100):\n",
    "    A_Jacobi = T_Jacobi*A_Jacobi_anterior+C_Jacobi\n",
    "    A_Jacobi_anterior = A_Jacobi\n",
    "\n",
    "display(\"A a las 100 iteraciones\" ,pd.DataFrame(A_Jacobi))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f016d489",
   "metadata": {},
   "source": [
    "Cambio de variables:\n",
    "\n",
    "$$A_1=0.270300=\\ln{b}; A_2=0.730104=\\ln{a}$$\n",
    "\n",
    "$$a=e^{0.730104}=2.075296; b=e^{0.270300}=1.310357$$\n",
    "\n",
    "Funcion aproximante:\n",
    "$$y=2.075296*1.310357^x$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 357,
   "id": "02812973",
   "metadata": {
    "scrolled": False
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7f8164bf44f0>]"
      ]
     },
     "execution_count": 357,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXQAAAD7CAYAAAB68m/qAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAAsTAAALEwEAmpwYAAAi90lEQVR4nO3de0BUZcIG8GcuDPdhYLiDSaIgoklKoWah2GolmtlF13StNNvczCw/123brbTLUn6rrlpqbbvWZ9a2uaYooaaSGl5SSxFv4Y24MwwMDDC3c74/TDYT5DIDZ2Z4fn/FwDnzhPh4eM973lcmiqIIIiJyeXKpAxARkWOw0ImI3AQLnYjITbDQiYjcBAudiMhNsNCJiNwEC52IyE0opQ6g1xshCO2fCq/V+kGnq+uERJ2P2bueq+YGmF0qzppdLpchMNC32c9JXuiCIHao0K8e66qYveu5am6A2aXiatk55EJE5CZY6EREboKFTkTkJljoRERuQvKbokRE3UXuyVJszCmAzmCCVu2JiamxGJoY7rDzs9CJiLpA7slSrMs6DbNVAADoDCasyzoNAA4rdQ65EBF1gY05BU1lfpXZKmBjToHD3oOFTkTUBXQGU7te7wgWOhFRF9CqPdv1ekew0ImIusDE1FiolNdWrkopx8TUWIe9B2+KEhF1gas3PjnLhYjIDQxNDHdogf8Sh1yIiNwEC52IyE2w0ImI3AQLnYjITbDQiYjcBAudiMhNsNCJiNxEq4WekZGBtLQ0xMfH4+zZswAAvV6PJ598EmPGjMG4cePwzDPPoKqqqtPDEhFRy1ot9FGjRmH9+vWIiopqek0mk2HmzJnIzs7Gli1b0KNHDyxZsqRTgxIR0Y21WujJycmIiIi45jWNRoOUlJSmj5OSklBcXOz4dEREbkYURdhqazvl3HaPoQuCgA0bNiAtLc0ReYiI3JYoiih9fy0uvvqnTjm/3Wu5LF68GD4+Ppg6dWqHjtdq/Tr83iEh/h0+VmrM3vVcNTfA7FJxdPaiL7ag9mAubpo6pVO+L3YVekZGBi5duoTVq1dDLu/Yxb5OVwdBENt9XEiIPyoqOufXls7G7F3PVXMDzC4VR2evP5WPH//5IfwGDYZn6q86fG65XNbihXCHC33p0qXIy8vD2rVroVKpOnoaIiK3Z9HpULLmXajCwhH+xEzIZLJOeZ9WC/21117D9u3bUVlZiccffxwajQbLli3D6tWrERMTg8mTJwMAoqOjsWrVqk4JSUTkqgSTCcWr/gbRZkXk7+ZA7uXdae/VaqG/9NJLeOmll657/cyZM50SiIjIXYiiiLJ1/4Cp8DIin5kLVXhE6wfZgU+KEhF1En12FmoPHYB2wkT4DUzq9PdjoRMRdQJj3glUfv4Z/JJvQ9B96V3ynix0IiIHM5eWoGTNO1BFRSP88c67CfpLLHQiIgeyGY0oWrEcMoUSUc88C7mnZ5e9NwudiMhBRJsNJWvfhaWyAhGzn4FHcEiXvj8LnYjIQSo++xT1J/MQ9uhv4BMX3+Xvz0InInKA6pw9qN65HZpRv0LAXamSZGChExHZqf5UPso//gg+/Qcg5JHJkuVgoRMR2cFcWorid1dBFRaGiFlPQ6ZQSJaFhU5E1EG2ujoUrVgKmVyOyDnPQeHjI2keu5fPJSJyd7knS7ExpwA6gwlatScmpsZiSHwwit9ZAatOh+gXFkAVEip1TBY6EdGN5J4sxbqs0zBbBQCAzmDCuqzTqN5TgtizZxA+cxa8+8RJnPIKDrkQEd3AxpyCpjK/ymwVkF3lC+34CVAPGSZRsuvxCp2I6AZ0BlOzrxs8fBE0zrm23uQVOhHRDWjVzT+6H+Tv1WVrtLQVC52I6AYmpsZCpby2KlVKOR4cEStRopax0ImIbmBoYjimpd6EAKEBEEUE+Xpg+r19MTQxXOpo1+EYOhHRDQiNjYjO/gizi4sQPX8hvHv1kjpSi3iFTkTUAtFmQ8mad2C6dBERT8126jIHWOhERM0SRRFl/7cOxhPHETp1epdsIWcvFjoRUTMKN3wKw96vETR2HDSpI6SO0yYcQyci+oXqPbtQ/ulnUA+/E9oJE6WO02YsdCKin6k9egTl6z9C4G2DETztMaeba34jHHIhIvpJ/ZnTKF37Lrxu7oX4/3lB0qVwO4KFTkQEoPHyJRSvXA6PkFBEPTsPii7c3NlRWOhE1O2Zy8tRtOx/Iff2RtS8F6Dw85M6Uoew0ImoW7NWV6No6dsQBQHR8+bDI0grdaQOY6ETUbdlq6vDj0uXwGqoRdSzz0MVESl1JLu0WugZGRlIS0tDfHw8zp492/T6hQsXMGnSJIwZMwaTJk3CxYsXOzMnEZFDCY2NKPrbX2EpK0XUM886/VOgbdFqoY8aNQrr169HVFTUNa+//PLLmDJlCrKzszFlyhT8+c9/7rSQRESOJFjMKF71NzRevPJIv09CP6kjOUSrhZ6cnIyIiIhrXtPpdMjPz0d6ejoAID09Hfn5+aiqquqclEREDiJarShZ8y7qT+UjbPoT8Lt1kNSRHKZDY+glJSUICwuD4qc5mgqFAqGhoSgpKXFoOCIiRxIFAaUfvA/jd8cQOmUqAu4YLnUkh5L8SVGttuPTg0JC/B2YpGsxe9dz1dwAszuCKIooWLUatYcOoOdvpiL6wQdaPcZZsrdVhwo9IiICZWVlsNlsUCgUsNlsKC8vv25opi10ujoIgtju40JC/FFRUdvu45wBs3c9V80NMLsjiKKIik8/RvXOnQgaOw6ed93dai5nyf5LcrmsxQvhDg25aLVaJCQkIDMzEwCQmZmJhIQEBAUFdTwlEVEnEEURlZ9/huqdO6C5e7RLLbbVXq1eob/22mvYvn07Kisr8fjjj0Oj0WDr1q145ZVXsHDhQrzzzjtQq9XIyMjoirxERO1SteUL6L/choDUkQiZ9GuXWmyrvWSiKLZ/vMOBOOTiWlw1u6vmBpjdHlXbMlG58d9QDxuOsMeegEze9kEJqbO3xOFDLkREzq4qOwuVG/8N/9uHtLvMXZX7/x8SUbej35GNys8+hV/y7Qif8WS3KHPACaYtEhE5kv6rHaj4dAN+GJCG3UIsdG/nQKv2xMTUWAxNDJc6XqdioROR29B/tQMVG9bjh8SR2Gy5CeYGEwBAZzBhXdZpAHDrUu8ev4cQkdu7WuZ+tw7Gbs/eMFuFaz5vtgrYmFMgUbquwUInIpen37m9qcwjnnoaOoOp2a9r6XV3wUInIpdWlZ2Fik8+ht+gK2UuUyqhVTe/fVxLr7sLFjoRuayqbZlNs1kiZl0pcwCYmBoLlfLaelMp5ZiYGitFzC7Dm6JE5HJEUURV5mbovvgP/FOGIPyJJyH7afVX4L83PjfmFEBnMHGWCxGRMxJFEZUb/w191laoh92BsMdmNDvPfGhiuNsX+C+x0InIZfx31cQdCEgdidBHp3Wbh4bagoVORC5BFASU/9+HqPl6DzR3j3b7hbY6goVORE5PtFpR+sH7qD10AEH3pUP7wIMs82aw0InIqQkWM0rWvAvjd8cQPPEhBN2XLnUkp8VCJyKnJTQ2oHjVCtSfykfoo9OgGTlK6khOjYVORE7JVleHouV/ReOliwh/4kmoh90hdSSnx0InIqdj0etRtPRtWMrLEfn0M/C7dZDUkVwCC52InIq5rBQ/Ll0CW20dop57AT59E6SO5DJY6ETkNBovXkTR8v8FRKDH/AXwurmX1JFcCgudiJxC/al8FK38GxR+voieNx+q8AipI7kcFjoRSa728CGU/n0tPELDEDVvPjwCA6WO5JJY6EQkKf3OHaj49GN49+6DyGfmQuHrK3Ukl8VCJyJJiIJwZZGtL7fB79bBCH/yKchVKqljuTQWOhF1OdFqRek//o7ag7lcZMuBWOhE1KVs9UYUv7MSDadPIXjiQwi8dyzXZXEQFjoRdRlLlQ5Fy5fCXFqC8BlPQj2UT386EgudiLpE46WLKPrbMohmE6LmPg/ffolSR3I7dhf67t27sXz5coiiCEEQMGfOHIwePdoR2YjITdR9/x1K1r4Lha8fohf+EZ5R0VJHckt2FbooiliwYAHWr1+PuLg4nD59Gr/+9a9x9913Q84bHEQEQP/VDlR88jE8e9yEqGfnQanRSB3Jbdl9hS6Xy1FbWwsAqK2tRWhoKMuciCDabDi/9n1UbM2Cb9KtiJj5FOReXlLHcmt2FbpMJsOyZcswe/Zs+Pj4wGg0Ys2aNY7KRkQuIPdkKTbmFEBnMEGr9sTE1Fjc3isAJWveRX3ecQSOvgfBDz3CaYldQCaKotjRg61WK2bOnIk5c+Zg8ODBOHLkCF544QVs3boVvnzai8jt7TlSiJWffQ+Txdb0mkopx7jGE+hz+Rhin3oS4ffwnlpXsesK/dSpUygvL8fgwYMBAIMHD4a3tzcKCgpwyy23tOkcOl0dBKH9/6aEhPijoqK23cc5A2bveq6aG3Du7P/MPHlNmQOA2SpgB2Iw4rk0hKcOcdrsrXHW77tcLoNW69f85+w5cXh4OEpLS3H+/HkAQEFBASorK3HTTTfZc1oichE6g6nZ1w1KX05LlIBdV+ghISF45ZVXMHfu3KYnvd58801oeBebqFvQqj2bLXWt2lOCNGT3LJfx48dj/PjxjshCRC5mwpBofLj9LCxQNL2mUsoxMTVWwlTdF287E1GHmIqKEPnvd3BPeS4Cf7og16o9Mf3evhiaGC5tuG6Kj/4TUbvVHTuCkvffg9xThXuenokH+vSROhKBhU5E7SAKAnRbvkDVli/gGXMzIn/3LHcXciIsdCJqE1u9EaXvrYHxxHGoh92B0GnTIffghhTOhIVORK0yFf2I4lUrYNFVIvTRaQgYkcY1zJ0QC52IbshwMBdl6/4Bubc3esxfCG+OlzstFjoRNUu0WlHxr09QvWsnvPvEIeKp2Vwp0cmx0InoOpYqHUrWvIvGgh+g+dUYhDz4MGRK1oWz458QEV3DmHcCJe+vgWixIuK3s+GffLvUkaiNWOhEBOBnUxIzN0MVGYXIp38HVXiE1LGoHVjoRARrTTVK3luDhtOnrkxJfPQ3kHtyPRZXw0In6ubqT+Wj5L3VEBobEfb4DATccafUkaiDWOhE3ZRos0G3eROqtmVCFRaO6BcWcPNmF8dCJ+qGLFVVKH1vNRrOnYV62HCEPjqNQyxugIVO5Gaa2+Pz56sf1h07gtJ/fgDRakP4jFlQDx0mYVpyJBY6kRvJPVmKdVmnYbYKAK7sKLQu6zQAIKVPECo++wQ1u3fB86aeiJj1NFThXObWnbDQidzIxpyCpjK/ymwV8Pmus4j413aYi35E4Oh7EDzxIT4o5Ib4J0rkRlra47OqzgJbrQFRzz0P3/5t28CdXA8LnciNtLTHZ4Dcgp6vvAalWi1BKuoq3IKOyI1MTI2FSnntX2sPuYiHxw5kmXcDLHQiN3J7rwDc71MKtaUOEEUE+Srx2NhEDOvPR/i7Aw65ELmJ+jOnUfrBe4itqsJL946Fdvx9vPHZzfBPm8jFCWYzdP/5HPqd2+EREooeC/8I79jeUsciCbDQiVxYw/nzKPvgPZhLSxAwIg0hD0/iE5/dGAudyAUJFguqtnyBqqytUGoCETVvPnwT+0sdiyTGQidyMY0XL6D0g/dhLi6CethwhEyeAoWPj9SxyAmw0IlchGAxQ7f5C+izs6AMCEDks/Pgd8tAqWORE2GhE7mAhh/OoeyfH8BcWgL18DsR8shkKHx8pY5FTsbuQjeZTHjjjTeQm5sLT09PJCUlYfHixY7IRtTtCY2NOP/ev1CyNQvKoCCOldMN2V3ob7/9Njw9PZGdnQ2ZTIbKykpH5CLq9ox5x1H20TpYdTpo0kYheOJDkHt5Sx2LnJhdhW40GrFp0ybk5ORAJpMBAIKDgx0SjKi7stYaUPHpBtQeyIUqIhID/vI6TMFRUsciF2BXoRcWFkKj0WDlypU4ePAgfH19MXfuXCQnJzsqH1G3IYoiDN/sR8Vnn0BoaEDQuPsRdF861JFBqKiolToeuQCZKIpiRw/Oy8vDgw8+iCVLlmDcuHH4/vvv8dvf/hY7duyAn5+fI3MSubWGomIUrF6LmuMn4J/QF71n/xY+N/WQOha5GLuu0CMjI6FUKpGeng4AGDhwIAIDA3HhwgUMGDCgTefQ6eogCO3/NyUkxN9lr1qYves5a27BYkbVtq3QZ22FzMMDodOmI+DOVBjlchh/yuus2duC2R1PLpdBq23+gtmuQg8KCkJKSgr279+P4cOH48KFC9DpdOjZs6c9pyXqFoz5J1G+/kNYysrgnzIEIY9MhjJAI3UscmF2z3J59dVX8eKLLyIjIwNKpRJvvfUW1Fx3majJLzdtvj85HL2OZqPu20PwCA3jVERyGLsLvUePHvjoo48ckYXI7TS3afOHOwtwn64Kd97/AALvuRdyD5XEKcldcIMLok7U3KbNVrkS+2JSoR13P8ucHIqFTtSJWty02Wjp4iTUHbDQiTqBYDFDl7kZaqux2c9r1VyznByPi3MROZAoiqg7+i0qP/sXLJUVGD0gDZstfjBb/zs1V6WUY2JqrIQpyV2x0IkcpPHyJVR88jEazp6BKioa0S8sQFxCPwT+YpbLxNRYDE0MlzouuSEWOpGdrDXVqPzPRhj274Xc1xehj/4GAXelQqZQAACGJoazwKlLsNCJOkgwm6HfkY2qbVshWi0IvHs0gtLHQ+HLdcpJGix0onYSBQG1B3NRufFzWPVV8L11EEIeegSqMF6Fk7RY6ETtUH8qHxWffQrT5UvwjLkZ4TNnwSe+r9SxiACw0InaxFRYiIrP/4X6vBNQarUInzkL/rcPgUzOmb/kPFjoRDdg0VVCt+k/MBz4BnJvbwQ/PAmatFF8wpOcEgudqBnWWgOqtm1Fze6vAACBo+9B0L1joeA6/+TEWOhEP2NraIB++5fQb8+GaDZBfcdwaMdPgEeQttmv/+VKipxjTlJioRMBEEwmVO/ZhaqsrRDq6uA3OBnBEyZCFRHZ4jHNraS4Lus0ALDUSRIsdOrWBIsFhr050G3NhK2mGj6J/RH8wEPwiolp9djmVlI0WwVszClgoZMkWOjULYlWK2r270PV1s2wVlXBOy4e2qeehk9cfJvP0dJKii29TtTZWOjUrYhWKwwHvkFV5hZYKivg1SsWYdOfgE+/RMhksnadS6v2bLa8uZIiSYWFTt2CYLWiZm8OqrZmwlJZAc+YmxH16DT49B/Q7iK/amJq7DVj6ABXUiRpsdDJrQkWCwzf7Mel7G0wlZfDM+ZmRE55FL4DBna4yK+6Ok7OWS7kLFjo5JYEsxk1+76G/sttsFZVwS+uD7STpzikyH+OKymSM2Ghk1sRGhtQvWc39Nu/hM1ggFfvPgib/gR6pg5BZWWd1PGIOhULndyCrbYW+q92oHrXVxDqjfBJSETQU+PgHRcPmUzm0KtyImfFQieXZtHpoN/xJWq+zoFoNsM36VYE3ZcO7168MUndDwudXJKpqAj6L7fBcOgAAMD/9hQE3TMWnlFREicjkg4LnVyGKIpoOHMa+uwsGE8ch0ylgmZkGgJ/dQ88tM2vtULUnbDQyemJNhtqjxyGfns2TBcvQOHvD+39D0AzchRXPyT6GRY6OS1bfT0M+76GfucOWKt08AgLR+i06VAPvQNyFdcjJ/olFjo5HXNFOaq/2gHDvr0QGhvhHReP0ClT4XvLQO4QRHQDDiv0lStXYsWKFdiyZQvi4uIcdVrqJprGx3duh/H77wC5HP633Y7Au8e0aeVDInJQoZ88eRLfffcdIiNbXjuaqDmCyQTDwVxUf7UT5qIfofDzR9B96QgYkQaPwMAbHsvNJYiuZXehm81mLFq0CEuWLMH06dMdkYm6AXNFOWr27ELN3r0Q6o3w7NEDYY89Af+UIW3ar5ObSxBdz+5CX758OcaPH48ePXp06HittuOzFEJC/Dt8rNS6Y3ZREFB97DuUbM2C/ugxQCaDdmgKIsbeB3W/hHY9zblpX26zm0ts2ncB40f0cWhuZ8Ds0nC17HYV+rFjx3DixAnMnz+/w+fQ6eogCGK7jwsJ8UdFRW2H31dK3S27tdYAw769qMnZA0tlBRRqNYLSxyPgrhHwCAyEGWj3OisV+oYWX28uX3f7njsLZnc8uVzW4oWwXYV++PBhnD9/HqNGjQIAlJaWYsaMGXjzzTcxfPhwe05NLk4URTScO4uanN2oO/ItRKsV3nHxCJ74EPwGDYZMad8vh9xcguh6dv2tmjVrFmbNmtX0cVpaGlavXs1ZLt2Yra4Ohtz9qPk6B+aSYsi9vRFw1wgEpI506GP53FyC6Hqch052uzrlsGZvTtPVuFevXgh7bAb8b7sdck/HXzVzcwmi6zm00Hft2uXI05GTs1brYfhmP2r27YWlvOynq/FUBNw5Ap4dvEneHtxcguhavEKndhEsFtQe+RaG/XthPHEcEEV4x8VDO+5++A1O5iP5RBJioVObNF6+BMM3+3D+0EFYDQYoNBoE3TsW6juGQxXGq2QiZ8BCpxZZa6pRe/AADLn7YSoshEypRFDKbfAcPAS+/QdwXRUiJ8NCp2sIJhP2fHkIW04ZUSN6QG01425lBIZPSYX/7UMQfnOEU87NJSIWOuHKE5wNZ07DkPsNDpwqw7bA22CVqwAZYPDwQ6ayH7RhfTGUa48TOTUWejcliiJMly6h9mAuDIcOwlZTDbmXF76+6QFYhWt/LMxWARtzCjijhMjJsdC7GXNJMQyHDqL20EFYykoBhQK+A26BeshQ+N6ShOq/7mv2uOaeyiQi58JC7wbMFeWoO3wItYcPwVR4GZDJ4B3fF0Fj7oXf4GQofH2bvpaP1BO5Lha6m7JUVqD2yLdXSvziBQCAV69eCJk8Bf7Jt0GpaX6tcT5ST+S6WOhuxFxRjroj36L228NNJe4ZczOCH3oE/sm3wSM4pNVz8JF6ItfFQndx5tIS1B75FnVHvoXp8iUAgGfPGAQ/+Aj8kpOhCglt9zn5SD2Ra2KhuxhRFGG6fAl1x46g7ugRmIuLAQBevWIR/PAk+A9KhkdI61fiROR+WOhOprl9Mof0DUHDubOo++4o6o4dhVWna7qxGTIiDX5Jg+ARFCR1dCKSGAvdiTS3T+Y/t+Sh7MPD6Kc7A5lSCZ/E/tCOmwC/gUlQ+LvW9lhE1LlY6E7k893nrtsn0wI5vtYOwqhJo+Gb2L9T1hYnIvfAQpeQaLOh8XwB6o5/D+Px71HlNRJoZqPkasED/oMGS5CQiFwJC72LWWsNKD95FKXfHIIx7wQEoxFQKODduw8C5YDecv0xfKiHiNqChd7JREFA44XzMOadQH3eCTRevACIIhT+avgNTILvLQPh068/FD4+eOgXY+gAH+ohorZjobeiuVknrc3RtlbrYczLQ/3JEzDmn7xyFS6TwevmXtCOn4Dou4ai3j/4uvXE+VAPEdmDhX4Dzc06WZd1GgCuKVnBZELDuTMwnjyJ+pN5MBcXAQAUAQHwG5gEn8QB8E3sD8VPy8/6hfijoYU1xflQDxF1FAv9BjbmFFw36+TqUrJJ3kbUn8pHff5JNBb8ANFqhUyphHdcPNTD7oBvYn+oontA1sxNTiKizuCWhd6RYZLmtLRkrK6mEYVvLAYAePboAc2ou+HTrz+8e/fhtEIikozbFXpbh0luRBRFWMrLEKgC9ObrP69R2BAx62l4902AUq12WHYiInu4XaHfaJikpUK/WuANZ86g/sxpNJw9Datej+F+McgKGwar7L/fJpVSjofvvQX+HOcmIifjdoXe4jDJz14XBQHmkhI0nD2DhrOnUX/2LGw11QCu3Mj0ie8L77h4xPRNQFgl8J+vz3PWCRE5Pbcr9JZ23An0UaAqOwsN586i4YdzEOrqAAAKjeZKgcfHwycuHh7hEdfcyBwWDgzrH9Fl+YmIOsrtCr25HXeUghXDz3+NyuMX4REWBr+Bt8I7Lg7ecfHwCA7hTBQicgt2Fbper8eCBQtw+fJlqFQq9OzZE4sWLUJQFy7lKooiLGVlaCg4h8aCHxDxww8YY/BAjnYQDEpfBMCEe0IbMGz0WHj36QNlgKbLshERdSW7Cl0mk2HmzJlISUkBAGRkZGDJkiV44403HBKuJeayMhTuzobu+Ek0nC+48iQmALm3N7x6xeKu2/pgTO/e8Lq5F+ReXp2ahYjIWdhV6BqNpqnMASApKQkbNmywO1RrKj79GMbj30MVGQm/WwfBu1dvePXuDVV4xHWP0xMRdRcOG0MXBAEbNmxAWlqao07Zooinn4FW7Ql9g9D6FxMRdRMyURRFR5zo1VdfRVlZGVauXAk5r5KJiLqcQ67QMzIycOnSJaxevbrdZa7T1UEQ2v9vSkiIPypaWODK2TF713PV3ACzS8VZs8vlMmi1fs1+zu5CX7p0KfLy8rB27VqoVCp7T0dERB1kV6GfO3cOq1evRkxMDCZPngwAiI6OxqpVqxwSjoiI2s6uQu/Tpw/OnDnjqCxERGQH3r0kInITLHQiIjch+VoucnnH11Gx51ipMXvXc9XcALNLxRmz3yiTw+ahExGRtDjkQkTkJljoRERugoVOROQmWOhERG6ChU5E5CZY6EREboKFTkTkJljoRERugoVOROQmJH/0v70uXLiAhQsXorq6GhqNBhkZGYiJiZE6VqsyMjKQnZ2NoqIibNmyBXFxcVJHajO9Xo8FCxbg8uXLUKlU6NmzJxYtWoSgoCCpo7XJ7Nmz8eOPP0Iul8PHxwd/+tOfkJCQIHWsNlu5ciVWrFjhUj83aWlpUKlU8PT0BADMnz8fd955p8Sp2sZkMuGNN95Abm4uPD09kZSUhMWLF0sdq21EFzNt2jRx06ZNoiiK4qZNm8Rp06ZJnKhtDh8+LBYXF4sjR44Uz5w5I3WcdtHr9eKBAweaPv7LX/4i/uEPf5AwUfsYDIam/96xY4c4YcIECdO0T15enjhjxgxxxIgRLvVz44o/51ctXrxYfP3110VBEERRFMWKigqJE7WdSw256HQ65OfnIz09HQCQnp6O/Px8VFVVSZysdcnJyYiIiJA6RodoNBqkpKQ0fZyUlITi4mIJE7WPv79/03/X1dVBJnO+BZeaYzabsWjRIrz88ssuk9nVGY1GbNq0CXPnzm36ngcHB0ucqu1casilpKQEYWFhUCgUAACFQoHQ0FCUlJS4zK//rk4QBGzYsAFpaWlSR2mXP/7xj9i/fz9EUcT7778vdZw2Wb58OcaPH48ePXpIHaVD5s+fD1EUMXjwYDz//PNQq9VSR2pVYWEhNBoNVq5ciYMHD8LX1xdz585FcnKy1NHaxKWu0El6ixcvho+PD6ZOnSp1lHZ5/fXXsWfPHsybNw9vvfWW1HFadezYMZw4cQJTpkyROkqHrF+/Hps3b8bnn38OURSxaNEiqSO1idVqRWFhIfr164eNGzdi/vz5mDNnDurq6qSO1iYuVegREREoKyuDzWYDANhsNpSXl7vsUIarycjIwKVLl7Bs2TLI5S71o9NkwoQJOHjwIPR6vdRRbujw4cM4f/48Ro0ahbS0NJSWlmLGjBnYt2+f1NHa5OrfSZVKhSlTpuDo0aMSJ2qbyMhIKJXKpmHdgQMHIjAwEBcuXJA4Wdu41N9KrVaLhIQEZGZmAgAyMzORkJDA4ZYusHTpUuTl5WHVqlVQqVRSx2kzo9GIkpKSpo937dqFgIAAaDQa6UK1waxZs7Bv3z7s2rULu3btQnh4OP7+979j+PDhUkdrVX19PWprawEAoihi27ZtLjOrKCgoCCkpKdi/fz+AK7PqdDodevbsKXGytnG5DS4KCgqwcOFCGAwGqNVqZGRkoFevXlLHatVrr72G7du3o7KyEoGBgdBoNNi6davUsdrk3LlzSE9PR0xMDLy8vAAA0dHRWLVqlcTJWldZWYnZs2ejoaEBcrkcAQEB+P3vf4/ExESpo7VLWloaVq9e7RLTFgsLCzFnzhzYbDYIgoDY2Fi89NJLCA0NlTpamxQWFuLFF19EdXU1lEolnnvuOaSmpkodq01crtCJiKh5LjXkQkRELWOhExG5CRY6EZGbYKETEbkJFjoRkZtgoRMRuQkWOhGRm2ChExG5if8HCB0SBDCGCZwAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x = np.linspace(0,6.5,100)\n",
    "y = 2.075296*(pow(1.310357,x))\n",
    "plt.plot(x, y, '-r', label='P(x)=(-18.008608114678815/x)+2.428870')\n",
    "\n",
    "plt.plot(datos_dataframe['X'], datos_dataframe['Y'], 'o')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2104fabe",
   "metadata": {},
   "source": [
    "# Punto f)\n",
    "\n",
    "Por descarte podemos decir que la funcion del punto d) no es adecuada ya que presenta una asintota horizontal en x~=7.41439, luego se mantiene cercana a 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 358,
   "id": "ddd7ca77",
   "metadata": {
    "scrolled": False
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7f8164141ff0>]"
      ]
     },
     "execution_count": 358,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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fGfMmGHwqGJPlmV0dAQeEtPR0YG8vDzI8vTarC1atAhOp3PIslhty6b83U6j4fF4kJ+fD0VRAACKoiAvLw8ejwd2u93g0cWepml44YUXUFRUZPRQYu7xxx/HihUrMGfOHKOHEhenTp1CdnY2nnzySbz99ttIS0vDunXrsGjRIqOHFjOSJOGxxx7DPffcg9TUVHR1deHpp582elhxEatt2fSKUhrV5s2bkZqaittvv93oocTUu+++i2PHjqGsrMzoocRNf38/Tp06hQULFuCll17CAw88gG9/+9vo7Ow0emgx09/fj6effhrbtm3DoUOH8NRTT+H+++9HV1eX0UObshIqEJxOJ5qamqCqKgBAVVU0NzcPK8emo8rKSnz66ad47LHHpl1JfaGjR4/i5MmTWLp0KYqKitDY2Ii1a9fijTfeMHpoMTNz5kxYLJbwLoSrrroKOTk5qKurM3hksXP8+HE0Nzfj6quvBgBcffXVSElJQW1trcEji71Ybcum95bhAg6HAy6XC9XV1QCA6upquFyuab+7aMuWLXj//fexdetW2Gw2o4cTc3fffTfeeOMNHDx4EAcPHkRBQQF27NiBa6+91uihxYzdbsfixYvx5ptvAgicgeL1enHRRRcZPLLYKSgoQGNjI06ePAkAqK2tRWtrK+bOnWvwyGIvVtuyhHtATm1tLcrLy9He3o7MzExUVlbikksuMXpYMfPxxx/D7XZj3rx5SE5OBgDMnj0bW7duNXhk8VNUVITt27fj8ssvN3ooMXXq1Ck89NBDOHfuHCwWC9avX48bbrjB6GHF1CuvvIJf/vKX4QPp9913H2666SaDR6WvRx55BPv370draytycnKQnZ2NPXv2xGRblnCBQEREkSXULiMiIhoZA4GIiAAwEIiIKIiBQEREABgIREQUxEAgIiIADAQiIgpiIBAREQDg/wP2KTiB214soQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x = np.linspace(0,10,100)\n",
    "y = (-18.008608114678815)/(x-7.41439)\n",
    "plt.plot(x, y, '-r', label='P(x)=(-18.008608114678815/x)+2.428870')\n",
    "\n",
    "plt.plot(datos_dataframe['X'], datos_dataframe['Y'], 'o')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ad659a7",
   "metadata": {},
   "source": [
    "Tambien podemos descartar la recta de minimos cuadrados, ya que tenemos la parabola disponible y esta presenta un error menor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 359,
   "id": "d1b160b4",
   "metadata": {
    "scrolled": False
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7f8166014b50>]"
      ]
     },
     "execution_count": 359,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x = np.linspace(0,6.5,100)\n",
    "\n",
    "y = 0.255529618189472*pow(x,2)-0.143398273502509*x+2.51714300600557\n",
    "\n",
    "plt.plot(x, y, '-g')\n",
    "\n",
    "x = np.linspace(0,6.5,100)\n",
    "\n",
    "y = 1.564444*x+0.749333\n",
    "\n",
    "plt.plot(x, y, '-r', label='P(x)=1.564444*x+0.749333')\n",
    "\n",
    "plt.plot(datos_dataframe['X'], datos_dataframe['Y'], 'o')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4c1a2927",
   "metadata": {},
   "source": [
    "Esto nos deja con la parabola de minimos cuadrados y el modelo exponencial.\n",
    "\n",
    "Al graficar ambos en un rango mas amplio, vemos que la exponencial crece mucho mas rapido que la parabola. Al alejarse del rango dado, vemos que la exponencial alcanza niveles absurdos (> 10^100 para 1 millon de subscriptores) mientras que la parabola se mantiene en amplitudes razonables.\n",
    "\n",
    "Ademas, el modelo exponencial fue calculado \"linealmente\" a traves de un cambio de variable, por lo que termina siendo inferior al modelo de parabola.\n",
    "\n",
    "Por lo tanto, el modelo que mejor se adapta en este caso es el de parabolas de minimos cuadrados.\n",
    "\n",
    "en el caso de los 20k subscriptores, ya no podemos basarnos en lo arrojado por la estimacion ya que se sale demasiado del rango original (200; 6500)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 360,
   "id": "56b548f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'exponencial: 3000 subscriptores -> 46692 visitas'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'exponencial: 7000 subscriptores -> 137659 visitas'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'exponencial: 20000 subscriptores -> 4622455 visitas'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'parabola: 3000 subscriptores -> 43867 visitas'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'parabola: 7000 subscriptores -> 140343 visitas'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'parabola: 20000 subscriptores -> 1018610 visitas'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7f8165fb1180>]"
      ]
     },
     "execution_count": 360,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x = np.linspace(0,20, 100)\n",
    "\n",
    "y = 0.255529618189472*pow(x,2)-0.143398273502509*x+2.51714300600557\n",
    "display (\"exponencial: 3000 subscriptores -> %d visitas\" %(10000*(2.075296*(pow(1.310357,3)))))\n",
    "display (\"exponencial: 7000 subscriptores -> %d visitas\" %(10000*(2.075296*(pow(1.310357,7)))))\n",
    "display (\"exponencial: 20000 subscriptores -> %d visitas\" %(10000*(2.075296*(pow(1.310357,20)))))\n",
    "display (\"parabola: 3000 subscriptores -> %d visitas\" %(10000*(0.255529618189472*pow(3,2)-0.143398273502509*3+2.51714300600557)))\n",
    "display (\"parabola: 7000 subscriptores -> %d visitas\" %(10000*(0.255529618189472*pow(7,2)-0.143398273502509*7+2.51714300600557)))\n",
    "display (\"parabola: 20000 subscriptores -> %d visitas\" %(10000*(0.255529618189472*pow(20,2)-0.143398273502509*20+2.51714300600557)))\n",
    "plt.plot(x, y, '-g',label='P(x)=0.255529618189472*x^2-0.143398273502509x+2.51714300600557')\n",
    "\n",
    "y = 2.075296*(pow(1.310357,x))\n",
    "plt.plot(x, y, '-r', label='P(x)=(-18.008608114678815/x)+2.428870')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
