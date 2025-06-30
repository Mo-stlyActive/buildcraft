import { SearchResponse } from '@/types/chat';

interface SearchResultsCardProps {
  searchResults: SearchResponse;
}

export default function SearchResultsCard({ searchResults }: SearchResultsCardProps) {
  const getCategoryColor = (category: string) => {
    switch (category.toLowerCase()) {
      case 'skills': return 'bg-blue-100 text-blue-800';
      case 'weapons': return 'bg-red-100 text-red-800';
      case 'armor': return 'bg-green-100 text-green-800';
      case 'spells': return 'bg-purple-100 text-purple-800';
      case 'items': return 'bg-yellow-100 text-yellow-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="bg-white border border-gray-200 rounded-lg p-6 shadow-lg max-w-2xl">
      {/* Header */}
      <div className="flex items-center mb-4">
        <span className="text-3xl mr-3">🔍</span>
        <div>
          <h3 className="text-xl font-bold text-gray-900">Search Results</h3>
          <p className="text-sm text-gray-600">Found {searchResults.results.length} items</p>
        </div>
      </div>
      
      {/* Reasoning */}
      {searchResults.reasoning && (
        <div className="mb-4">
          <h4 className="font-semibold text-gray-800 mb-2 flex items-center">
            <span className="text-lg mr-2">💭</span>
            Analysis
          </h4>
          <p className="text-gray-700 leading-relaxed text-sm bg-gray-50 p-3 rounded-lg">
            {searchResults.reasoning}
          </p>
        </div>
      )}
      
      {/* Results */}
      <div className="mb-4">
        <h4 className="font-semibold text-gray-800 mb-3 flex items-center">
          <span className="text-lg mr-2">📋</span>
          Items Found
        </h4>
        <div className="space-y-3">
          {searchResults.results.map((result, index) => (
            <div key={index} className="border border-gray-200 rounded-lg p-3 hover:bg-gray-50 transition-colors">
              <div className="flex items-center justify-between mb-2">
                <h5 className="font-medium text-gray-900">{result.name}</h5>
                <div className="flex items-center gap-2">
                  <span className={`px-2 py-1 text-xs font-medium rounded-full ${getCategoryColor(result.category)}`}>
                    {result.category}
                  </span>
                  <span className="text-xs text-gray-500">
                    Score: {result.score.toFixed(2)}
                  </span>
                </div>
              </div>
              <p className="text-sm text-gray-600">Type: {result.type}</p>
              {result.properties && Object.keys(result.properties).length > 0 && (
                <div className="mt-2">
                  <p className="text-xs text-gray-500 mb-1">Properties:</p>
                  <div className="flex flex-wrap gap-1">
                    {Object.entries(result.properties).map(([key, value]) => (
                      <span key={key} className="text-xs bg-gray-100 text-gray-700 px-2 py-1 rounded">
                        {key}: {String(value)}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
      
      {/* Suggestions */}
      {searchResults.suggestions && searchResults.suggestions.length > 0 && (
        <div className="mb-4">
          <h4 className="font-semibold text-gray-800 mb-2 flex items-center">
            <span className="text-lg mr-2">💡</span>
            Suggestions
          </h4>
          <ul className="text-sm text-gray-700 space-y-1">
            {searchResults.suggestions.map((suggestion, index) => (
              <li key={index} className="flex items-start">
                <span className="text-blue-500 mr-2">•</span>
                {suggestion}
              </li>
            ))}
          </ul>
        </div>
      )}
      
      {/* Action Buttons */}
      <div className="flex flex-col sm:flex-row gap-2">
        <button className="flex-1 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors font-medium">
          🔍 Refine Search
        </button>
        <button className="flex-1 px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors font-medium">
          💾 Save Results
        </button>
        <button className="flex-1 px-4 py-2 bg-gray-500 text-white rounded-lg hover:bg-gray-600 transition-colors font-medium">
          🔗 Share
        </button>
      </div>
    </div>
  );
} 