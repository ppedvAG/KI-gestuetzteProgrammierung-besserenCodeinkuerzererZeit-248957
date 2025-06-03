using NUnit.Framework;

namespace ArrayHelperTests
{
    [TestFixture]
    public class ArrayHelperTests
    {
        private ArrayHelper _arrayHelper;

        [SetUp]
        public void Setup()
        {
            _arrayHelper = new ArrayHelper();
        }

        [Test]
        public void SumEvenNumbers_WithEmptyArray_ReturnsZero()
        {
            // Arrange
            int[] numbers = new int[0];

            // Act
            int result = _arrayHelper.SumEvenNumbers(numbers);

            // Assert
            Assert.That(result, Is.EqualTo(0));
        }

        [Test]
        public void SumEvenNumbers_WithOnlyEvenNumbers_ReturnsCorrectSum()
        {
            // Arrange
            int[] numbers = new int[] { 2, 4, 6, 8 };

            // Act
            int result = _arrayHelper.SumEvenNumbers(numbers);

            // Assert
            Assert.That(result, Is.EqualTo(20));
        }

        [Test]
        public void SumEvenNumbers_WithOnlyOddNumbers_ReturnsZero()
        {
            // Arrange
            int[] numbers = new int[] { 1, 3, 5, 7 };

            // Act
            int result = _arrayHelper.SumEvenNumbers(numbers);

            // Assert
            Assert.That(result, Is.EqualTo(0));
        }

        [Test]
        public void SumEvenNumbers_WithMixedNumbers_ReturnsSumOfEvenNumbers()
        {
            // Arrange
            int[] numbers = new int[] { 1, 2, 3, 4, 5, 6 };

            // Act
            int result = _arrayHelper.SumEvenNumbers(numbers);

            // Assert
            Assert.That(result, Is.EqualTo(12));
        }

        [Test]
        public void SumEvenNumbers_WithNegativeNumbers_ReturnsCorrectSum()
        {
            // Arrange
            int[] numbers = new int[] { -2, -1, 0, 1, 2 };

            // Act
            int result = _arrayHelper.SumEvenNumbers(numbers);

            // Assert
            Assert.That(result, Is.EqualTo(0));
        }
    }
} 