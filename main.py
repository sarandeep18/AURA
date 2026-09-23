from Engines.Data.load_dataset import load_dataset
from Engines.Data.validate_dataset import validate_dataset
from Engines.Data.clean_missing import clean_missing_values
from Engines.Data.remove_duplicates import remove_duplicates
from Engines.Analytics.summary import summary
from Engines.Analytics.data_types import data_types
from Engines.Analytics.mean import mean
from Engines.Analytics.median import median
from Engines.Analytics.mode import mode
from Engines.Analytics.minimum import minimum
from Engines.Analytics.maximum import maximum
from Engines.Analytics.standard_deviation import standard_deviation
from Engines.Analytics.correlation import correlation
from Engines.Recommendation.content_based import content_based
from Engines.Recommendation.collaborative_filtering import collaborative_filtering
from Engines.Recommendation.similar_products import similar_products
from Engines.Recommendation.trending_products import trending_products
from Engines.Recommendation.category_recommendation import category_recommendation
from Engines.Recommendation.personalized_recommendation import personalized_recommendation
from Engines.Recommendation.recommendation_score import recommendation_score
from Engines.Recommendation.recommendation_summary import recommendation_summary
from Engines.Visualization.bar_chart import bar_chart
from Engines.Visualization.line_chart import line_chart
from Engines.Visualization.pie_chart import pie_chart
from Engines.Visualization.scatter_plot import scatter_plot
from Engines.Visualization.histogram import histogram
from Engines.Visualization.box_plot import box_plot
from Engines.Visualization.heatmap import heatmap
from Engines.Visualization.visualization_summary import visualization_summary
from Engines.Reporting.report_manager import report_manager


def analytics_engine(dataset):

    dataset = summary(dataset)
    dataset = data_types(dataset)
    dataset = mean(dataset)
    dataset = median(dataset)
    dataset = mode(dataset)
    dataset = minimum(dataset)
    dataset = maximum(dataset)
    dataset = standard_deviation(dataset)
    dataset = correlation(dataset)

    return dataset
def recommendation_engine(dataset):

    dataset = content_based(dataset, "Laptop")
    dataset = collaborative_filtering(dataset, "C001")
    dataset = similar_products(dataset, "Laptop")
    dataset = trending_products(dataset)
    dataset = category_recommendation(dataset, "Laptop")
    dataset = personalized_recommendation(dataset, "C001")
    dataset = recommendation_score(dataset)
    dataset = recommendation_summary(dataset)

    return dataset
def visualization_engine(dataset):

    dataset = bar_chart(dataset)
    dataset = line_chart(dataset)
    dataset = pie_chart(dataset)
    dataset = scatter_plot(dataset)
    dataset = histogram(dataset)
    dataset = box_plot(dataset)
    dataset = heatmap(dataset)
    dataset = visualization_summary(dataset)

    return dataset

print("===================================")
print("     AURA DATA ENGINE STARTED")
print("===================================")

# Load Dataset
dataset = load_dataset()

# Validate Dataset
if validate_dataset(dataset):

    # Clean Missing Values
    dataset = clean_missing_values(dataset)

    # Remove Duplicate Values
    dataset = remove_duplicates(dataset)
    print("\nAURA Data Engine Completed Successfully!")
    print("\n===============================")
    print("\n   AURA Engaged    ")
    print("\n===============================")
    dataset = analytics_engine(dataset)
    print("\n AURA Analytics Engine engaged")
    dataset = recommendation_engine(dataset)
    print("\n AURA Recommendation Engine engaged")
    dataset = recommendation_engine(dataset)
    print("\nAURA Recommendation Engine engaged")
    dataset = visualization_engine(dataset)
    print("\nAURA Visualization Engine engaged")
    dataset = report_manager(dataset)
    print("\nAURA Reporting Engine engaged")
    print("\n===================================")
    print("   AURA BACKEND COMPLETED")
    print("===================================")
else:

    print("\nAURA Data Engine Stopped.")